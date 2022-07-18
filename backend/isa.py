''' File that implements ISA. Is very slow, and poorly implemented. Not my code but eh.'''
from collections.abc import Iterable
import math
import numpy as np

## Have to refactor so works with numpy
def get_temperature(h):
    ''' International Standard Atmosphere 1976 temperature as a function
		of height in meters
	 	https://en.wikipedia.org/wiki/Barometric_formula#Pressure_equations
        If array calls recursively, stupid but oh well 
	'''
    if not isinstance(h, Iterable):
        if h < 11000:
            hb = 0
            Tb = 288.15
            Lb = -0.0065
            T = Tb + Lb * (h - hb)
        elif h < 20000:
            hb = 11000
            Tb = 216.65
            Lb = 0
            T = Tb + Lb * (h - hb)
        elif h < 32000:
            hb = 20000
            Tb = 216.65
            Lb = 0.001
            T = Tb + Lb * (h - hb)
        elif h < 47000:
            hb = 32000
            Tb = 228.65
            Lb = 0.0028
            T = Tb + Lb * (h - hb)
        elif h < 51000:
            hb = 47000
            Tb = 270.65
            Lb = 0
            T = Tb + Lb * (h - hb)
        elif h < 71000:
            hb = 51000
            Tb = 270.65
            Lb = -0.0028
            T = Tb + Lb * (h - hb)
        elif h < 84852:
            hb = 71000
            Tb = 214.65
            Lb = -0.002
            T = Tb + Lb * (h - hb)
        else:
            T = False
        return T
    else:
        T = np.zeros_like(h)
        for i, height in enumerate(h):
            T[i] = get_temperature(height)
        return T
            

def get_density(h):
    ''' Returns International Standard Atmosphere 1976 density as a function
		of height in meters
		https://en.wikipedia.org/wiki/Barometric_formula#Density_equations
        If an array is passed recursively calles the function
	'''
    R_star = 8.3144598  # J/(mol·K)
    g0 = 9.80665
    M = 0.0289644
    if not isinstance(h, Iterable):
        if h < 11000:
            hb = 0
            rhob = 1.225
            Tb = 288.15
            Lb = -0.0065
            rho = rhob * (Tb / (Tb + Lb * (h - hb)))**(1 + (g0 * M /
                                                            (R_star * Lb)))
        elif h < 20000:
            hb = 11000
            rhob = 0.36391
            Tb = 216.65
            rho = rhob * math.exp(-g0 * M * (h - hb) / (R_star * Tb))
        elif h < 32000:
            hb = 20000
            rhob = 0.08803
            Tb = 216.65
            Lb = 0.001
            rho = rhob * (Tb / (Tb + Lb * (h - hb)))**(1 + (g0 * M /
                                                            (R_star * Lb)))
        elif h < 47000:
            hb = 32000
            rhob = 0.01322
            Tb = 228.65
            Lb = 0.0028
            rho = rhob * (Tb / (Tb + Lb * (h - hb)))**(1 + (g0 * M /
                                                            (R_star * Lb)))
        elif h < 51000:
            hb = 47000
            rhob = 0.00143
            Tb = 270.65
            rho = rhob * math.exp(-g0 * M * (h - hb) / (R_star * Tb))
        elif h < 71000:
            hb = 51000
            rhob = 0.00086
            Tb = 270.65
            Lb = -0.0028
            rho = rhob * (Tb / (Tb + Lb * (h - hb)))**(1 + (g0 * M /
                                                            (R_star * Lb)))
        elif h < 84852:
            hb = 71000
            rhob = 0.000064
            Tb = 214.65
            Lb = -0.002
            rho = rhob * (Tb / (Tb + Lb * (h - hb)))**(1 + (g0 * M /
                                                            (R_star * Lb)))
        else:
            rho = 0
        return rho
    else:
        rho = np.zeros_like(h)
        for i, height in enumerate(h):
            rho[i] = get_density(height)
        return rho


def get_pressure(h, atm=False):
    '''
		In PA, Returns the pressure according to as a function of height
        in meters
		https://en.wikipedia.org/wiki/Barometric_formula#Derivation
	'''
    R_star = 8.3144598  # J/(mol·K)
    g0 = 9.80665
    M = 0.0289644
    p = get_density(h) * R_star * get_temperature(h) / M
    if atm == True:
        p = get_density(h) * R_star * get_temperature(h) / (M * 101325)
    return p
