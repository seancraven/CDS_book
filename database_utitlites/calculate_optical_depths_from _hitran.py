"""
    Script for calculating absorption coefficient as a function of
    altitude for 6 most abundant GHGs.
    
    
    The main work is handled by the HITRAN api.
    Calculating the absorption coefficients once
    and building a database after that enables much faster
    atmospheric model calculations after initial setup.

    The outputs are stored in a local SQLite database.
    The schema for the database is straightforward, and can be found at:
    weblink.
"""
import os
import sys
from typing import Any, Tuple
import sqlite3
from sqlite3 import Error
import numpy as np
from tqdm import tqdm
import isa
from optical_depth_functions import optical_depth


class HiddenPrints:
    """Suppresses prints to console"""

    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


with HiddenPrints():
    import hapi


class Ghg:
    """
    Records ghg abundance in ppb ghg abundance assumed constant. Up to
    implemented ceiling of 10 km.

    This is the same assumption as taken by MODTRAN, which achieves
    accuracies
    better than 1k accuracy on thermal brightness temperature.
    """

    ppm = {"CO2": 411 * 1000, "CH4": 1893, "N2O": 327, "H2O": 25 * 10**6}
    ids = {"CO2": 2, "CH4": 6, "N2O": 4, "H2O": 1}


def ghg_lbl_download() -> object:
    """
    Downloads and Stores Line by line Data for 4 most abundant ghg.
    If further gases are required add a name and HITRAN id to
    molecule_id_dict. Data is collected from HITRAN.

    Assumes only most abundant isotopologue is required.

    This additionally creates a local database. This database is queried
    from in the ghg_od_calculate().
    """
    with HiddenPrints():
        hapi.db_begin("./spectral_line.db")
        isotopologue = 1  # only want main isotopologue
        min_wavenumber = 0
        max_wavenumber = 4000  # spectral flux density
        # in (watts m^(-2)m^-1) is negligible beyond this region
        for gas, _id in Ghg.ids.items():
            hapi.fetch(
                gas, _id, isotopologue, min_wavenumber, max_wavenumber
            )


def ghg_od_calculate(gas: str, alt: float):
    """
    Calculates the optical density of a km of atmosphere, due to a
    single gas.

    Args:
        gas (str): string of gas name, valid gasses found in Ghg.
        alt (float): midpoint altitude of km block of atmosphere.

    Returns: (np.array, np.array): wavenumber and optical density arrays
    of same shape.
    """
    temp = isa.get_temperature(alt)
    pressure = isa.get_pressure(alt)
    press_0 = isa.get_pressure(0)
    with HiddenPrints():
        nu, coef = hapi.absorptionCoefficient_Voigt(
            SourceTables=gas,
            Environment={"T": temp, "p": pressure / press_0},
            Diluent={"air": 1.0},
        )

        od = optical_depth(alt - 500, alt + 500, Ghg.ppm[gas], coef)
    return nu, od, coef


def pragma(connection: sqlite3.Connection):
    """Function to improve performance of sqlite database"""
    connection.execute("PRAGMA journal_mode = OFF;")
    connection.execute("PRAGMA synchronous = 0;")
    connection.execute("PRAGMA cache_size = 1000000;")  # give it a GB
    connection.execute("PRAGMA locking_mode = EXCLUSIVE;")
    connection.execute("PRAGMA temp_store = MEMORY;")


def create_connection(db_file: str):
    """
    Creates a connection to database object.

    Args:
        db_file (str): /path/to/database/name.db

    Returns:
        database connection object:
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)


def create_table(connection: sqlite3.Connection, create_table_sql: str):
    """
    Creates a table from sql statement.

    Args:
        connection: Database to create table in.
        create_table_sql: SQL command to create table string.
    """
    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_query(
    connection: sqlite3.Connection, table: str, **values: Any
):
    """
    Adds an entry to a tabel.

    Args:
        connection: Database to insert into
        table: Table of database to insert into.
    Keyword Args:
        values: of the form column=entry. The entry must have the same
        type as specified in the database.
    Returns:
        int: Last row number appended to table
    """

    sql = f"INSERT INTO {table}"
    columns = "("
    value_var = "("
    for column in values.keys():
        columns += column + ","
        value_var += "?,"
    columns = columns[:-1] + ")"
    value_var = value_var[:-1] + ");"
    sql += columns + "VALUES" + value_var
    try:
        cur = connection.cursor()
        cur.execute(sql, list(values.values()))
        connection.commit()
        return cur.lastrowid
    except Error as e:
        print(e)


def column_comparison_query(
    connection: sqlite3.Connection,
    table: str,
    operator: str,
    **columns_val,
):
    """
    Function that performs a query on a table with the op, returns all
    columns of a row that obeys the query conditions.

    Args:
        connection: Database to query.
        table: table to query.
        operator: WHERE column {operator} value. The comparison operator
            for a SQL statement.

    *Kwargs:
        columns: column_name=value, for the comparison operator.
    Returns:
        tuple: values from table.
    """
    vals = []
    sql = f"SELECT * from {table} WHERE"
    for i, (column, value) in enumerate(columns_val.items()):
        if i != 0:
            sql += " and"
        sql += f" {column} {operator} ?"
        vals.append(value)
    sql += ";"
    try:
        cur = connection.cursor()
        cur.execute(sql, vals)
        query_result = cur.fetchall()
        return query_result
    except Error as e:
        print(e)


def main():
    ghg_lbl_download()
    conn = create_connection(r"./optical_depth.db")
    # Use sqlite3 PRAGMA for faster loading
    pragma(conn)
    if conn is not None:
        create_table_gas_sql = """CREATE TABLE IF NOT EXISTS gases (
                                    mol_id integer PRIMARY KEY, 
                                    mol_name text NOT NULL, 
                                    mol_ppm real NOT NULL
                                    );"""
        create_table_abs_coef_sql = """CREATE TABLE IF NOT EXISTS 
        optical_depths (
                                        mol_id INTEGER, 
                                        altitude REAL NOT NULL, 
                                        wave_no  REAL NOT NULL,
                                        optical_depth REAL NOT NULL,
                                        abs_coef REAL NOT NULL,
                                        PRIMARY KEY (mol_id, altitude, 
                                        wave_no),
                                        FOREIGN KEY (mol_id) REFERENCES 
                                        gases (mol_id)
                                    );"""
        create_table(conn, create_table_gas_sql)
        create_table(conn, create_table_abs_coef_sql)
        print("created tables")
    else:
        print("Didnt Work")
    #
    # Populating Gases
    for (mol_name, mol_id), (_, mol_ppm) in zip(
        Ghg.ids.items(), Ghg.ppm.items()
    ):
        try:
            insert_query(
                conn,
                "gases",
                mol_name=mol_name,
                mol_id=mol_id,
                mol_ppm=mol_ppm,
            )
        except sqlite3.IntegrityError:
            query = column_comparison_query(
                conn, "gases", "=", mol_id=mol_id
            )
            if not query:
                print(f"{mol_name} already in database")
    altitudes = np.arange(500, 30500, 1000, dtype=float)
    #
    # Populating optical_depths
    for gas, _id in tqdm(Ghg.ids.items()):
        for alt in tqdm(altitudes, leave=False):
            query = column_comparison_query(
                conn, "optical_depths", "=", altitude=alt, mol_id=_id
            )
            if not query:
                wave_number, od, coef = ghg_od_calculate(gas, alt)
                for nu, tau, coef in zip(wave_number, od, coef):
                    try:
                        insert_query(
                            conn,
                            "optical_depths",
                            _id,
                            alt,
                            nu,
                            tau,
                            coef,
                        )
                    except sqlite3.IntegrityError:
                        query = column_comparison_query(
                            conn,
                            "optical_depths",
                            "=",
                            mol_id=_id,
                            altitude=alt,
                            wave_no=nu,
                        )
                        if not query:
                            print(
                                f"""Failed to add \n
                                molecule:{gas} \n
                                altitude:{alt} \n
                                wavenumber:{nu}
                                """
                            )
            else:
                pass


if __name__ == "__main__":
    main()
