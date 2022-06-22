#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


path_global = 'http://berkeleyearth.lbl.gov/auto/Global/Land_and_Ocean_summary.txt'
temp_data_global = pd.read_csv(path_global, header=None, delimiter=' ', comment = '%')


# In[10]:


temp_data_global


# In[ ]:




