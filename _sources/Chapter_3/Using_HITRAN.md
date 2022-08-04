# HITRAN
The HITRAN database, an acronym for high-resolution transmission molecular absorption database, was initially intended as purely a database to store the infrared properties of the atmosphere, which is what we use it for. However, the scope has grown massively and the about page is quite [informative](https://hitran.org/about/).
## Using the HITRAN-API
```{margin}
An application programming interface(API) provides a method for two programmes to communicate. Typically they provide a way to obscure the inner workings of a program but enable a user to have a fixed interface that produces a fixed output. A good example is the c based arrays implemented by numpy. One doesn't need to know how the arrays are implemented assides that doing [vectorised](https://blog.paperspace.com/numpy-optimization-vectorization-and-broadcasting/) operations on them is really fast, and consistent. 
```
For the book user, the author has built a small API on top of that of the HITRAN-API. This is intended,  to make the process of going from absorption spectrum to atmospheric radiation much more simple.
 ```{note}
 In addition, the HITRAN-API can be quite confusing as it is a 20000 line single file. 
 ``` 
Use of the HITRAN-API can be quite straight forward, A short run-through of downloading and calculating the absorption spectrum for $\textrm{CO}_2$ follows. 
```python
import hapi 
hapi.begin("path/to/your/local/hapi/database/")
hapi.fetch(
    TableName: str,
    Hitran_molecule_id: int,
    Molecule_isotopologue: int,
    nu_min: float,
    nu_max: float,
)
```
This command first checks your local database for the table name, if it is not found then it downloads all of the hitran parameters for that molecule number in the wavenumber range $[\nu_{min}, \nu_{max}]$. The hitran [molecule](https://hitran.org/docs/molec-meta/) and [isotopologue](https://hitran.org/docs/iso-meta/) numbers can be found on the website with their respective formulae. 

Then from this the API provides functionality to calculate the absorption coefficients in $molecules/ cm^2$ :
```python
wavenumber_array, absorbtion_coef_array = hapi.absorptionCoefficient_Voigt(
            SourceTables=TableName,
            Environment={"T": some_temperature, "p": some_pressure},
            Diluent={"air": 1.0},
        )
```
The hapi function family `absorptionCoeffient_Lineshape` Takes a table name, the argument to the fetch function, and in a dictionary temperature and pressure values, these are key in calculating line intensity, the area under a peak, and broadening. The final diluent parameter, takes a dictionary of atmospheric constituents. It has a parameter `"air"`, which corresponds to earth's atmosphere. However, you can pass a dictionary of the form: 
```python
{
"gas_0": fractional_concentration_0,
"gas_1": fractional_concentration_1,
etc...
}
```
Where, the gas names are strings of their formulae, and the table names. This function outputs a tuple of arrays, with the desired values. Further, additional parameters can be tweaked, such as how far each broadening function extends, thresholds for calculations to be performed and others found in the [documentation](https://hitran.org/static/hapi/hapi_manual.pdf). 

In the lineshape family, avalible shapes are Doppler(gaussian), Lorentz, Voight, and Hartmann-Trann a more computationally intensive, but improved shape{cite}`Hartmann-Trann`, which is beyond the scope for this book. 

These are the basic functions used in obtaining line-shapes, with which to calculate optical depth.

## Using the SimpleTrans package

The SimpleTrans package, which you will have installed if you clone the environment for the book or find it here, link to github.. discuss download. 

before, diving into using the package, a high level overview of what it does is usefull. 
After you have downloaded the package, it runs calculate_optical_depths_from_hitran.py. When this script is run in the `main()` function, the absorption spectra from hitran are downloaded. Then a relational database is created. 
```{mermaid}
erDiagram
    gases 
    gases{
    int mol_id
    string mol_name
    float mol_ppm
    }
    
    optical_depths{
    int mol_id PK
    float altitude PK
    float wave_no PK
    float optical_depth
    float abs_coef
    }
 ```
