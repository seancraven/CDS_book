## The Optical Depths Database

To understand why the data is pre-calculated it is worth looking at the orders of magnitude of the calculations and what they involve when implemented in python. As mentioned previously, The HITRAN database stores the spectral line intensity for many GHGs in our model. We include only four. However, each of these gases in the range $[200,4000] cm^{-1}$ has of the order 10,000 data points for the spectral line intensity. So when calculating the absorption coefficient and optical depth for each altitude on the grid, we store around 50 million rows. In each row an absorption coefficient, a wavenumber, an optical depth and a molecule id are stored. 
This is by no means a lot of data for modern hardware. However, doing the calculations on the fly is prohibitively expensive. Due to the nature of the broadening and conversion between spectral line intensity and absorption coefficient. This is the operation where the voight profile is applied and must be done on each entry in the array. 

Thus, precalculating all the values required for the model and storing them in a database was not only a good excuse to introduce databases but also means that the atmosphere profile can be very flexible and fast to use. 
```{note}
If you are not experienced with relational databases a short introduction is [provided](../Database_Chapter/Database_intro_1.md)
```

The database and atmosphere model are handled by the SimpleTrans package, which is discussed in more detail in its own [section](../Chapter_SimpleTrans/SimpleTrans.md).  

The database that is created, after the, installing the package stores the optical depths and absorption coefficients of $\textrm{CO}_2$, $\textrm{CH}_4$, $\textrm{H}_2\textrm{O}$ and $\textrm{N}_2\textrm{O}$ in the optical depths table. Each gas is recorded with altitudes in 1km spacings from $500 m$ to $30,500 m$. These altitudes correspond to the midpoints of the altitude grid. The wavenumber range recorded is between $200 cm^{-1} and $4000 cm^{-1}. This wavenumber range provides nearly complete coverage of all longwave radiation outgoing from Earth.

Each gas is stored with its formulae and ppm concentration.

The database is definitely not absolutely necessary, and one could achieve similar results with a .txt file, however, with 50 million rows, it would be an unwieldy file, and dealing with less than all the data would be challenging. Further, the database provides the ability to work with small subsets of the data in a jupyter notebook or python file. Its schema is presented below. It is a straightforward solution; however, it solves the problem well. 

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
