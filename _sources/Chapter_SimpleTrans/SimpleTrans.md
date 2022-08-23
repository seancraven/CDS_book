# SimpleTrans
The simple trans package is the result of walking through Chapter 3 in building a radiative transfer model. However, its aim is to provide a straightforward introduction to radiation modelling, and working with outside APIs and databases. 

## Using the SimpleTrans package

The SimpleTrans package, which you will have installed if you clone the environment for the book or find it [here](https://pypi.org/project/SimpleTrans/) 
It can be installed using pip separately however, 
```shell
pip install simpletrans
```
From with this done you local database must be populated. This is done by running the main script: 
```shell 
simpletrans -m 
```
This will ask you to select a local folder for the database to be installed into, this must alredy exist. Currently, with the default gases, it takes up 3Gb, and about an hour to install. 

From here all the functions and classes can be accessed. For more information, each function is documented in their respective files in their docstring. 

The [atmosphere_grid] page has exemplar implementations of the module. 

## Structure and Overview
before, diving into using the package, a high level overview of what it does is useful.
After you have downloaded the package, one runs `__main__.py`. When this script is run the absorption spectra from HITRAN are downloaded. Then a [relational database](rd) is created. This database is populated, by calculating absorption coefficients$(molecules/cm^2)$ and optical depths, of blocks of atmosphere, given by:
\begin{equation}
OD = k(\nu, T, P)\cdot [X],
\end{equation}
where k is the absorption coefficient, $[X]$, is the path integral of molecular density over the block of atmosphere
\begin{equation}
[X] = \int_{h_i}^{h_{i+1}} n(T,p)dh.
\end{equation}

Where h_i, is the start of the atmosphere block, n is the number density of the molecule. This is repeated over every gas for every altitude for all wavenumbers. 

To enable these calculations, there are files which contain functions to help calculate these quantities. isa.py implements the [standard atmosphere](../Chapter_2/lorentzian_broadening.ipynb), to obtain temperature and pressures as a function of altitude and plank.py implements the plank function in a manner which has convenient default behaviour. 

Finally, radiative_transfer.py implements a class called atmosphere grid. This models the atmosphere as a coarse altitude grid and a fine wavenumber grid of spacings, $1 km$ and $1 cm^{-1}$, respectively. The mean optical depth is queried from the database for the wavenumber bin and evaluated at the midpoint of the altitude block. The mean value and midpoint provide reasonable approximations to the quantities values in the region. 

The database solution was chosen to speed up the process of the calculations, as doing them in real time can be very slow. 

For these gridded values the [two stream equations](../Chapter_2/radiative_transfer.ipynb) are solved for the upward fluxes by the method AtmosphereGrid.up_flux(). This produces an output of a flux grid that models the transfer of radiation out of the atmosphere. 

For more detail on individual functions, Every functions is documented with a docstring. 

## Exercises
1. Calculate the maximum standard deviation of the averages of the optical depths for $\textrm{CO}_2$, where the bins are $1 cm^{-1}$ wide and centred on the integer wavenumbers. Is the standard error large in comparison to the mean?
2. Using the provided database plot the difference of the absorption coefficient for $\textrm{CO}_2$ at $0 km$ and $1 km$ elevation in ISA atmosphere. 
```{tip}
There are premade queries in the optical_depths_from_hitran.py file, which could be imported or copied and pasted.
```





