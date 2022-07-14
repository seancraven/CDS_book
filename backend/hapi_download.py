'''
    File to download main gases for CDS book

    The files are downloaded to the data_base_path location
    It is currently set up so that it makes a new folder hapi_db
    
    Adding New Gases: 
    you can download your own gases by editing this file and adding
    them to gas_id_dict. The key of the dict is the name of the table 
    !!!NOT!!! the gas. The gas is defined by the dictionary entry, the 
    integerwhich corresponds to the molecule ID on https://hitran.org/lbl/. 
'''
import hapi
if __name__ == '__main__':
    data_base_path = 'hapi_db'
    hapi.db_begin(data_base_path)
    gas_id_dict = {'CO2': 2, 'H2O':1 , 'CH4': 6, 
                   'NH3': 11, 'N2O': 4, 'O2': 7,
                   'N2': 22}
    for gas, id in gas_id_dict.items():
        hapi.fetch(gas, id, 1,0,4000)
    