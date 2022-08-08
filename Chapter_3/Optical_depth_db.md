## The Optical Depths Database
The optical depths and other associated data is stored in a SQLite3 relational Database. There is a short [section](../SimpleTrans/SimpleTrans_1.md) on the advantage of this format. 

The database that is created, after the installing the package stores the optical depths and absorption coefficients of $\textrm{CO}_2$, $\textrm{CH}_4$, $\textrm{H}_2\textrm{O}$ and $\textrm{N}_2\textrm{O}$ in the optical depths table for altitudes in 1km spacings from $500 m$ to $30,500 m$, these values correspond to the midpoints of the altitude grid. The wavenumber range recorded is between $200 cm^{-1} and $4000 cm^{-1} this provides close to complete coverage of all longwave radiation outgoing from earth.

Each gas is stored with its formulae and ppm concentration. The need for all this data is explored more fully in the next section.

This data is calculated and stored once, because it is computationally expensive to calculate the values each time one wants to calculate them. This does reduce flexibility because there is a defined number of datapoints one can access, however, the pre computation was decided on so that day to day functionality was optimized.

The database is definitely not necessary and one could achieve similar results with a .txt file, however there are about 50 million rows, making it and unwieldy file. Further, the database provides the ability to work with small subsets of the data in a jupyter notebook or python file. Its schema is presented below. 

```{mermaid}   
:align: center
:caption: the entity relationship diagram for the optical_depths.db sqlite3 database.
erDiagram
    gases ||--|{optical_depths: ""
    gases{
    mol_id int PK
    mol_name string
    mol_ppm float
    }
    optical_depths{
    mol_id int PK "FK"
    altitude float PK
    wave_no float PK
    optical_depth float
    abs_coef float
    }
```
