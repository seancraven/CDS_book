'''
    File for radiation functions.
'''
from typing import Any
import numpy as np
from gas import Gas
from plank import plank_nu
import isa
def delta_flux(gas: Gas, incident_flux: Any, alt_2: float, alt_1: float=0, steps: int=10):
    ''' The change in incoming flux between two altitude in a number of steps
        for a single instance of the gas class
        Arguments:
            gas: instance of gas.py Gas class
            incident_flux: flux before calculations
            alt_1: start altitude in meters
            alt_2: final altitude in meters
            steps: number of steps altitude is broken into
            see gas.tau_for_whole atmosphere for more details.
        Returns:
            flux array of the same sape as the absorbtion coefficient
    '''
    tau = gas.tau_for_whole_atmosphere(alt_1,alt_2,steps)
    if alt_1 == 0:
        flux = np.array(np.exp(-tau)*incident_flux) \
            + plank_nu(gas.nu,isa.get_temperature(alt_2),flux=True)
    else :
        flux = np.array(np.exp(-tau)*incident_flux)
    return flux

def multigas(gases: list[Gas],alt_2,steps: int= 10, alt_1: float=0):
    ''' Performs The delta_flux operation on multiple Gases.
        The function returns a list of arrays the i-th entry of each of the lists
        has the same dimentions.
        Arguments:
            gases: List of Gas classes
            alt_2: stop atltitude.
            alt_1: start altitude default = 0.
            steps: number of steps altitude is broken into.
        Returns:
            outgoing_flux: list of arrays of the outgoing flux values.
            nuspec: list the wavenumber values for each gas.
            incident_fluxes: the incoming flux before absorbtion.
    '''
    incident_fluxes = []
    nuspec = []
    outgoing_flux = []
    for i,gas in enumerate(gases):
        incident_fluxes.append(plank_nu(gas.nu, isa.get_temperature(alt_1),flux = True))
        nuspec.append(gas.nu)
        outgoing_flux.append(delta_flux(gas,incident_fluxes[i],
        alt_2=alt_2,
        alt_1=alt_1,
        steps=steps)
        )
    return outgoing_flux , nuspec , incident_fluxes
