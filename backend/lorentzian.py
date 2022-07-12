'''
    File with functions for implementation of broadening.
'''
import numpy as np
import pandas as pd
from scipy.signal import find_peaks
from scipy.stats import cauchy
import isa
import gas

def main_peaks(gas: 'gas.Gas', quantile: float=0.99, start: int=0, stop: int=None):
    ''' Finds the main peaks of a gas's absorbtion spectra
        by default returns the top one percent of peaks.
        Arguments:
            gas: a gas class from ../gas.py
            threshold: 1 - percentage of peaks kept
            start: index where looking for peaks start
            stop: index where looking for peaks stop
            final 2 arguments used when only looking across small range of wavelengths
        Returns:
            peaks: array with only main peaks of size absorbtion_coeff
    '''
    absorbtion_coeff = np.array(gas.absorbtion_coeff)[start:stop]
    peaks , _  = find_peaks(absorbtion_coeff)
    if quantile:
        mean_height = np.quantile(absorbtion_coeff[peaks],quantile)
    else:
        mean_height = 0
    peaks = np.array((absorbtion_coeff[peaks] > mean_height)*peaks)
    peaks = peaks[peaks != 0]
    return peaks

def gamma(gas: 'gas.Gas',altitude: float):
    ''' Implementation of broadening factor gamma
        Arguments:
            gas: gas class from ../gas.py
            altitude: altitude in m
        Returns:
            gamma array
    '''
    t_ref = 296 ###K
    pressure = isa.get_pressure(altitude,atm = True)
    temperature = isa.get_temperature(altitude)
    n_air = gas.n_air
    p_self = pressure*gas.pv*isa.get_density(altitude)/isa.get_density(0)
    t_frac = (t_ref/temperature)**n_air
    return t_frac*(gas.gamma_air*(pressure-p_self)+gas.gamma_self*p_self)

def lorentzain_fit(gas: 'gas.Gas',altitude: float,threshold: float=0.99, start: int=None, stop: int=None):
    ''' Fuction to apply lorentzian lineshape to the main peaks
        I think this might have the larges perf overhead and might need to be redesigned
    '''
    peaks = main_peaks(gas,start=start, stop=stop, quantile=threshold)#find peaks for gas
    n_peak = np.shape(peaks)[0]#number of peaks
    if isinstance(gas.absorbtion_coeff, pd.DataFrame):
        spec_copy = np.array(gas.absorbtion_coeff.iloc[start:stop].copy())
    else:
        spec_copy = np.array(gas.absorbtion_coeff[start:stop].copy())
    spec_copy[peaks] = 0
    ###For loop applies a lorentzian fit
    ### Applies the lorenzian profile of a central peak between n_peak_coverage on either side
    ### Larger gamma values require larger values For n_peak_coverage, small
    ### gamma means that the profile is deltafunction like and doesn't effect
    ### further out peaks.
    n_peak_coverage = 1 ###Th
    for i in range(0,(n_peak)):
        if i < n_peak_coverage :
            sl_ = 0
            slp = 0
        if i >= n_peak -n_peak_coverage:
            sl_ = int(peaks[i-n_peak_coverage])
            slp = int(peaks[-1])
        if i>= n_peak_coverage and i< n_peak-n_peak_coverage:
            sl_ =int(peaks[i-n_peak_coverage])
            slp = int(peaks[i+n_peak_coverage])
        if isinstance(gas.absorbtion_coeff, pd.DataFrame):
            spec_copy[sl_:slp] += (gas.absorbtion_coeff.iloc[start:stop]).iloc[peaks[i]]\
                *cauchy((gas.nu.iloc[start:stop]).iloc[sl_:slp]\
                    ,(gas.nu.iloc[start:stop]).iloc[peaks[i]],(gamma(gas,altitude).iloc[peaks[i]]))
        else:
            spec_copy[sl_:slp] += (gas.absorbtion_coeff[start:stop])[peaks[i]]\
            *cauchy((gas.nu[start:stop])[sl_:slp]\
                ,(gas.nu[start:stop])[peaks[i]],(gamma(gas,altitude)[peaks[i]]))
    return spec_copy
