"""
    File with plank function implementation that is convinient for this
    project.
"""
import numpy as np
import scipy.constants as cst


def plank(
    x, temperature: int, flux: bool = False, units="cm", is_wavelength=True
):
    """Plank Function, wavelength or frequency
    Args:
        x: an array or list, in wavlength or frequency(nu)
        Flux: Boolean Value for False returns radiance
        units: "cm", "m" or "um" where "um" are micrometers
        is_wavelength: If true evaluates x in terms of wavelenth
            else evalutes x in terms of frequency
    Returns: returns all values in x evaluated with plank"""
    if is_wavelength:
        return plank_lambda(x, temperature, flux, units)
    else:
        return plank_nu(x, temperature, flux, units)


def plank_lambda(wavelength, temperature: int, flux=False, units="cm"):
    """Plank Function as a function of Wavelength
    Args:
        x: an array or list, in wavlength
        temperature: temperature in K
        Flux: Boolean Value for False returns radiance
        units: "cm", "m" or "um" where "um" are micrometers
    Returns: returns all values in x evaluated with plank
    """
    if units == "m":
        k = 1
    elif units == "cm":
        wavelength = wavelength / 100
        k = 1 / 100
    elif units == "um":
        k = 10**-6
        wavelength = wavelength * 10**-6
    if flux:  ### Returns Flux x in w/(m^2 cm^-1)
        pifac = cst.pi
    else:  ### Returns Radiance in w/(m^2 cm^-1 ster)
        pifac = 1
    c_1 = 2 * cst.h * cst.c**2 * k
    c_2 = cst.h * cst.c / cst.k
    return (
        pifac
        * c_1
        / wavelength**5
        * (1 / (np.exp(c_2 / (wavelength * temperature)) - 1))
    )


def plank_nu(nu_, temperature: int, flux=False, units="cm"):
    """Plank Function as a function of wavenumber
    Args:
        nu_: an array or list, in wavenumber
        temperature: temperature in K
        Flux: Boolean Value for False returns radiance
        units: 1/ "cm", "m" or "um" where "um" are micrometers
    Returns: returns all values in x evaluated with plank
    """
    if units == "m":  ####These are inverse units
        k = 1
    elif units == "cm":
        nu_ = nu_ * 100
        k = 100
    elif units == "um":
        k = 10 * 6
        nu_ = nu_ * 10**6
    c_1 = 2 * cst.h * cst.c**2 / k**2
    c_2 = cst.h * cst.c / cst.k
    if flux:  ### Returns Flux in w/(m^2 cm^-1)
        pifac = cst.pi
    else:  ### Returns Radiance in w/(m^2 cm -1 ster)
        pifac = 1
    return (
        pifac
        * c_1
        * nu_**3
        / (np.exp(c_2 * nu_ / temperature) - 1)
        * 10**6
    )


#%%
