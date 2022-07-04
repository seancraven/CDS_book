#!/usr/bin/env python
# coding: utf-8

# ## Global Temperature Predictions
# 
# This section uses global temperature data combined with global $\textrm{CO}_2$ concentration and warming data provided by the IPCC to compare a simple model with Global warming estimates laid out in the Special Report on Emission Scenarios(SRES).

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dur_utils import colours
from numpy.lib.stride_tricks import sliding_window_view
from scipy.optimize import curve_fit


# The global Temperature data is taken from Berkley Earth. The temperature data has missing fields as with the Global $\textrm{CO}_2$ data. Further, the date is formatted awkwardly into a fixed width table format with commented-out headers. Finally, the global temperature data is seasonal. A Fourier-based fit could be applied similarly to that performed in the section on Global $\textrm{CO}_2$ data. Because this section is not looking for a functional form, an average is more straightforward to implement.
# 
# After cleaning the data of null fields, a moving average can be used to remove the seasonal trends.

# In[23]:


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


# In[24]:


# Format date 
null_sum = (temp_data.isna()).values.sum(axis=0)
pd.DataFrame(data=null_sum,
    index=temp_data.columns,
    columns=['Number of Null Values']
    )


# In[25]:


#Drop NA
temp_data = temp_data.dropna()


# In[26]:


# Sliding window weighted average:
slv = sliding_window_view(temp_data, 120, 0)
time_midpoint = np.mean(slv[:,-1,:], axis=1)
win_ave_temp = slv[:,2,:]
win_ave_unc =  slv[:,3,:]


# In[6]:


fig, ax = plt.subplots(1, 1, figsize = (10, 6))
ave_temp = np.mean(win_ave_temp,axis=1)
ave_unc = np.mean(win_ave_unc, axis=1)

lb = ave_temp - ave_unc
ub = ave_temp + ave_unc

ax.plot(time_midpoint,
    ave_temp,
    color=colours.durham.ink
    )
ax.fill_between(time_midpoint,
    lb,
    ub,
    color = colours.durham.ink,
    alpha=0.2
    )
ax.set_xlabel('Window Midpoint /Year')
ax.set_ylabel('10 Year Moving Average of \n     Land Average Temperature Anomaly /$^{\circ}C$'
    );


# ## Predictions
# Global temperatures provide an interesting case study for a further introduction to predictive modelling. There has already been substantial warming compared to the period from $1850-1900$. This period is set as a pre-industrial baseline{cite}`preindbaseline`. Further temperature rises will continue to increase the occurrence of extreme weather events and myriad other consequences, with an etire [IPCC](https://www.ipcc.ch/sr15/) report dedicated to the consequences of warming over $1.5^\circ C$. The special report on emission scenarios(SRES){cite}`SRES` produced by the IPCC in 2000, details multiple families of emission scenarios with their associated warming. 
# 
# These scenarios are developed using six independent models. Such models use economic driving forces and predict the consequences of changing macro-economic behaviour, for example, the percentage of fossil fuel used compared to renewables. 
# 
# These highly detailed models are not suitable for this section. Using $\textrm{CO}_2$ concentration, an overly simplistic model can be formed to determine the change in temperature over the next 80 years.
# The three scenarios that will be investigated are inspired by Durham Universities' lack-lustre commitment to a net-zero commitment.
# 1. No reduction in emissions rates by 2030 and net-zero by 2050.
# 2. Net-zero by 2030, no further reductions
# 3. Net-zero by 2030, and then reducing total atmospheric carbon at the same rate it is currently produced. 
# The relationship between $\textrm{CO}_2$ concentration used is:
# ```{math}
# T(C) = T_0 + S \log_2(C/C_0).
# ```
# Where $C$ is the concentration of $\textrm{CO}_2$ and $S$ is a fitted sensitivity factor.

# ## Current Warming trend 

# In[7]:


def  moving_ave_frame(df:pd.DataFrame, window:int)->pd.DataFrame:
    'Applies a moving average'
    slv = sliding_window_view(df, window, axis=0)
    moving_averages = np.mean(slv, axis=2)
    ma_df = pd.DataFrame(moving_averages,columns=df.keys())
    return ma_df

def lb_ub(values, sigma):
    lb = values - sigma
    ub = values + sigma
    return lb, ub


# In[8]:


trend_data = temp_data[temp_data['dt'] > 1960]
trend_ave = moving_ave_frame(trend_data,120)
lb, ub = lb_ub(trend_ave['monthly_anomaly'], trend_ave['monthly_anomaly_unc'])


# In[21]:


def P1(x, a0, a1):
    return a0 + a1*x

trend_fit, trend_error = curve_fit(P1, trend_ave['dt'],
    trend_ave['monthly_anomaly'],
    sigma=trend_ave['monthly_anomaly_unc']
    )
gradient_lb =  trend_fit[1] - trend_error[1,1]
gradient_ub = trend_fit[1] + trend_error[1,1]


# In[22]:


lb, ub = lb_ub(trend_ave['monthly_anomaly'], trend_ave['monthly_anomaly_unc'])
#Plotting
fig, ax = plt.subplots(1,1, figsize=(10, 6))
time = np.linspace(2017.3, 2055, 300)
plt.fill_between(trend_ave['dt'], lb, ub, alpha=0.2,
    color=colours.durham.ink)
plt.plot(trend_ave['dt'],  trend_ave['monthly_anomaly'],
    c=colours.durham.ink,
    label='Data')
plt.plot(time, P1(time, *trend_fit),
    linestyle='--',
    color=colours.durham.ink,
    label='Linear Trend')
plt.fill_between(time, P1(time, trend_fit[0], gradient_lb),
    P1(time, trend_fit[0], gradient_ub))
ax.set_xlabel('Window Midpoint /Year')
ax.set_ylabel('10 Year Moving Average of \n     Land Average Temperature Anomaly /$^{\circ}C$'
    );
#Warming Targets
x = np.linspace(1960,2055,100)
y = np.ones_like(x)
plt.plot(x, y*1.5, color=colours.durham.red,
    label='$1.5^\circ C$ Warming',
    linestyle='--'
    )
plt.plot(x, y*2, color=colours.durham.red,
    label='$2.0^\circ C$ Warming',
    linestyle='--'
    )
plt.legend();


# With a simple linear extrapolation of the Berkeley Earth temperature data, one can see that if the current rate of warming persists, then keeping the Global Temperature anomaly below $1.5^\circ C$ is unlikely, moving into the future. However, this simple model is just for getting a feeling of the data. By combining this dataset with the Global $\textrm{CO}_2$ data the correlation of these datasets i
# 

# 
