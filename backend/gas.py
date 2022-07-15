'''
    File Containing Classes to manage the hitran database files
'''
import glob
import isa
import numpy as np
from scipy import constants as cst
import pandas as pd
import lorentzian


class Gas():
    ''' Gas Class which takes hitran files from CSV to Dataframe'''

    ### The Path is to the 'somegas'.csv file
    ### Uses the coustom format for the HITRAN data
    def __init__(self,
                 path: str,
                 relative_atomic_mass: float,
                 ppm: float = 415.1):
        hitran_data = pd.read_csv(path)
        self.nu_ = hitran_data['nu']
        self.nu_unit = '$cm^-1$'
        self.absorbtion_coeff = hitran_data['sw']
        self.absorbtion_coeff_unit = r'$cm^-1/molecule \cdot cm^-1'
        self.relative_atomic_mass = relative_atomic_mass
        self.relative_atomic_mass_unit = '$g/mol'
        self.data = hitran_data
        self.gamma_air = hitran_data['gamma_air']
        self.gamma_self = hitran_data['gamma_self']
        self.n_air = hitran_data['n_air']
        self.ppm = ppm  ##Parts per million
        self.p_v = ppm / 10**6  ###Fractional content per volume

    def tau_for_whole_atmosphere(self,
                                 alt_1: int,
                                 alt_2: int,
                                 steps: int = 10):
        ''' Function to Calculate optical thickness for a particular gas.
            breaks the atmosphere up into a number of steps between
            alt_1 and alt_2. alt_1 < alt_2 is enforced.
            Arguments:
                alt_1: start altitude in meters
                alt_2: stop altituse in meters
                steps: number of bands of altitude, equally spaced.
                    the altitude bands are governed by np.lispace(alt_1, alt_2, steps)
            Returns:
                tau: optical thickness parameter arrray of same shape as gas wavenumbers
        '''
        altitudes = np.linspace(alt_1, alt_2, steps)
        delta_alt = abs(altitudes[0] - altitudes[1]) * 100
        tau = np.zeros_like(self.nu_)
        for i, alt in enumerate(altitudes):
            no_mol = isa.get_density(alt) / 1000 * self.p_v / \
                (self.relative_atomic_mass) * cst.N_A * delta_alt
            tau += lorentzian.lorentzain_fit(self, alt) * no_mol
        return tau


class GasCrossection():
    ''' Gas class analogue for shortwave crossections'''
    def __init__(self, path: str, relative_atomic_mass, ppm):
        self.relative_atomic_mass = relative_atomic_mass  ### relative atomic mass g/mol
        self.path = path
        self.entries = len(crossection_from_csv(glob.glob(path + '*')[0]))
        self.nu_ = hitran_crossection_nu(
            glob.glob(path + '*')[0], self.entries)
        self.temps = list(crossections_temp_dataframe(self.path).columns)
        self.ppm = ppm  ### parts per million of the gas

    def get_corossection_at_t(self, temp):
        ''' Crossections are recorded for specific temperatures of gas.
            This fuction returns the crossction with the temperature closest to
            the temperature which the crossection was recorded at.
            Arguments:
                temp: Temperature in K
            Returns:
                crossection_df: crossection dataframe
        '''
        crossections_df = crossections_temp_dataframe(self.path)
        headers = list(crossections_df.columns)
        new_head = [int(i) for i in headers]
        temp = np.argmin(abs(temp - new_head))
        return crossections_df.iloc[:, temp]

    def crossection_temps(self):
        ''' Function to get crossection temperatures'''
        return self.temps


def crossection_from_csv(path):
    ''' Load crossection file'''
    csec = pd.read_csv(path, delimiter=" ", skiprows=1, header=None)
    csec = np.array(csec.iloc[:, 1:])
    csec = csec.flatten()
    return csec[:-1]


### Extracts the maxima and minima from the string at the top of the crossection file
def hitran_crossection_nu(
    path, entries
):  ###Returns 1D Array of NU values with the same number of entries as the
    ''' unsure'''
    data = open(path)
    first_line = str(data.readlines(1)[0])
    i = 0
    stops = 0
    zeros = 0
    jj = 0
    while zeros < 1:
        jj = jj + 1
        zeros = first_line[:jj].count('O')
    while stops < 1:
        i = i + 1
        stops = first_line[:i].count('.')
    j = i
    while stops < 2:
        j = j + 1
        stops = stops = first_line[:j].count('.')
    wave_start = float(first_line[i:j])
    wave_stop = float(first_line[jj:i])
    nu = np.linspace(wave_start, wave_stop, entries)
    return nu


def crossections_temp_dataframe(path):
    '''unsure'''
    all_crossect_paths = glob.glob(path + '*')
    entries = len(crossection_from_csv(glob.glob(path + '*')[0]))
    header = []
    corossections = np.zeros((entries, len(all_crossect_paths)))
    i = 0
    for path in all_crossect_paths:
        header.append(path[46:49])
        corossections[:, i] = crossection_from_csv(path)
        i = i + 1
    corossections = pd.DataFrame(corossections, columns=header)
    return corossections


class HitranConstants:
    ''' Class to store HITRAN constants.'''
    tref = 296
    pref = 1 * 10**5
