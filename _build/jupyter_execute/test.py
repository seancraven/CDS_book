#!/usr/bin/env python
# coding: utf-8

# In[1]:


def per(x, a_1, a_2, omega_1, omega_2, C):
    return a_1*np.cos(omega_1*x) + a_2*np.sin(omega_2*x) + C
    

# Fit Coefs
lower_bound = [-10,-10, 0, 0, -10]
upper_bound = 10
p0 = [5,5,100,100,0]
##Unweighted Least Squares Global
p1_res_fit, p1_res_error = scipy.optimize.curve_fit(per,
    co2_data_ml['decimal date']-co2_data_ml['decimal date'].iloc[0],
    rs_ml_p1,
    sigma=co2_data_ml['sdev'],
    p0=p0,
    #bounds=(lower_bound, upper_bound)
    )
#chisq
y_p1_res = per(co2_data_ml['decimal date'], *p1_res_fit)
rs_ml_res_p1 = y_p1_res-rs_ml_p1
chisq_res_p1 = np.sum(((rs_ml_res_p1)
    / np.mean(co2_data_ml['sdev']))**2
    )
#P3
p3_res_fit, p3_res_error = scipy.optimize.curve_fit(per,
    co2_data_ml['decimal date']-co2_data_ml['decimal date'].iloc[0],
    rs_ml_p3,
    sigma= co2_data_ml['sdev'], 
    #bounds=(lower_bound, upper_bound),
    p0=p0
    )
#chisq
y_p3_res = per(co2_data_ml['decimal date'], *p3_res_fit)
rs_ml_res_p3 = y_p3_res-rs_ml_p3
chisq_res_p3 = np.sum(((rs_ml_res_p3)
    / np.mean(co2_data_ml['sdev']))**2
    )
print(p3_res_fit)
plt.plot(co2_data_ml['decimal date'], rs_ml_p3)
plt.plot(co2_data_ml['decimal date'], y_p3_res)
However, as can be seen in the figure abvoe of an  

