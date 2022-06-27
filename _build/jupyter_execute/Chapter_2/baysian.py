#!/usr/bin/env python
# coding: utf-8

# ## Global Temperature Predictions
# 
# This section uses global temperature data in combination with global $CO_2$ concentration and warming data provided by the IPCC to make Global warming estimates. Similar calculations have been done with more complex models. However, the takeaway conclusions are similar.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dur_utils import colours
from numpy.lib.stride_tricks import sliding_window_view


# In[2]:



def yymmdd(temperature_data_frame: pd.DataFrame) -> pd.DataFrame:
    ''' inplace string date to float date'''
    result = np.zeros_like(temperature_data_frame['dt'])
    for ii, i in enumerate(temperature_data_frame['dt']):
        string = i.split('-')
        [yy, mm, dd] = [int(j) for j in string]
        result[ii] = yy + mm/12 + dd/365
        result = np.array(result, dtype=float)
    temperature_data_frame['dt'] = result


# The global Temperature data is taken from Berkley Earth. Want to write about the data collection methods from before 1950.
# The temperature data has missing fields as with the global $CO_2$ data. Further, the date is formatted awkwardly and needs to be converted into a float for easy processing. Finally the global temperature data is seasonal. Thus an averaging needs to be applied because the temperature data has known uncertainties a moving average can be applied to remove the seasonal trends.

# In[3]:


path = '/home/sean/Downloads/GlobalTemperatures.csv'
temp_data = pd.read_csv(path)
# Format date 
yymmdd(temp_data)
# Find NA
null_sum = (temp_data.isna()).values.sum(axis=0)
pd.DataFrame(data=null_sum,
    index=temp_data.columns,
    columns=['Number of Null Values']
    )
#Drop NA
temp_data = temp_data.dropna()



# In[4]:


print('Temperatures and Uncertainties are positive:\n', temp_data.all()>0)


# In[5]:


# Sliding window weighted average:
slv = sliding_window_view(temp_data, 120, 0)
print(slv.shape)
time_midpoint = np.mean(slv[:,0,:], axis=1)
win_ave_temp = slv[:,1,:]
win_ave_unc =  slv[:,2,:]


# In[6]:


fig, ax = plt.subplots(1, 1, figsize = (10, 6))
ave_temp = np.mean(win_ave_temp,axis=1)
ave_unc = np.mean(win_ave_unc, axis=1)


lb = np.array(ave_temp
    - ave_unc
    )
ub = np.array(ave_temp
    + ave_unc
    )
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
ax.set_ylabel('10 Year Moving Average of \n     Land Average Temperature / $^{\circ}C$'
    );


# ## Predictions
# There i

# In[ ]:




