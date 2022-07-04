#!/usr/bin/env python
# coding: utf-8

# ## Three Models 
# The three hypothetical scenarios inspired by 2030 net-zero commitments 
# 1. No reduction in emissions rates by 2030 and net-zero by 2050.
# 2. Net-zero by 2030, no further reductions.
# 3. Net-zero by 2030, from 2030 begin reducing total atmospheric carbon at the same rate it is currently produced. 

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dur_utils import colours
from numpy.lib.stride_tricks import sliding_window_view
from scipy.optimize import curve_fit
from scipy import stats


# In[2]:


path = "http://berkeleyearth.lbl.gov/auto/Global/Complete_TAVG_complete.txt"
#Formatting be data
colnames=['year', 'month', 'monthly_anomaly', 'monthly_anomaly_unc',
    'yearly_anomaly', 'yearly_anomaly_unc', '5yearly_anomaly',
    '5yearly_anomaly_unc', '10yearly_anomaly', '10yearly_anomaly_unc',
    '20yearly_anomaly', '20yearly_anomaly_unc'
    ]
temp_data = pd.read_fwf(path, skiprows=34, names=colnames)
temp_data['dt'] = temp_data['month']/12 + temp_data['year']
#remove be moving averages
temp_data.drop( columns=['yearly_anomaly', 'yearly_anomaly_unc',
    '5yearly_anomaly', '5yearly_anomaly_unc', '10yearly_anomaly',
    '10yearly_anomaly_unc', '20yearly_anomaly', '20yearly_anomaly_unc'],
    inplace=True
    )


# ## Determining the sensitivity coefficient
# The functional form of the model 
# ```{math} 
# T(C) = T_0 + S \log_2(C/C_0).
# ```
# Only has one free parameter. This corresponds to the sensitivity of the model. Because the equation is linear in $\log(C)$ an analytic solution can be found using the least-squares method.
# 

# In[3]:


def TofC(C: pd.DataFrame, S: int) -> pd.DataFrame:
    ''' Model fuction for Temperature and CO_2 relationship.'''
    C_0 = 
    T_0 = 
    return T_0 + np.log2(C/C_0)*S 

