'''
    File with reigligh utilities.
'''
import numpy as np
from gas import Gas
def reigligh_crossection(wavenumber):
###Note that this crossection is accurate for 0.25 to 1 *10^-6um##1000-4000 cm^-1
    ''' Calculates religh crossection for different wavenumber.'''
    wavenumber = wavenumber/10000
    numerator = 1.0455996 -341.29061*(wavenumber)**2 -0.90230850*wavenumber**(-2)
    denominator = 1+0.0027059889*(wavenumber)**2- 85.968563*wavenumber**(-2)
    return numerator/denominator

def rayligh_optical_depth(wavenumber):
    ''' Returns religh optical depth for different wavenumber.'''
    sigma = reigligh_crossection(wavenumber)
    return 0.0021520*sigma

# Wavenumber thingy not sure when used
def wavenumber_concantenate(gas: Gas, upper_lim):
    ''' No Idea '''
    gas_nu = np.array(gas.nu).flatten()
    nu_ = np.linspace(gas_nu[-2], upper_lim,1000)
    nu_ = np.hstack([gas_nu, nu_])
    return nu_