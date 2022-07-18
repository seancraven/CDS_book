main_ghg = list(molecule_id_dict)
p_ground = isa.get_pressure(0)
p_upper = isa.get_pressure(30000)
t_upper = isa.get_temperature(30000)
abs_coef_ground = []
abs_coef_p_upper = []
abs_coef_t_upper = []
abs_coef_upper = []
for gas in main_ghg:
    abs_coef_ground.append(hapi.absorptionCoefficient_Voigt(
        SourceTables=gas)
    )
    abs_coef_p_upper.append(hapi.absorptionCoefficient_Voigt(
        SourceTables=gas, 
        Environment={'T':296,'p':p_upper/p_ground})
    )
    abs_coef_t_upper.append(hapi.absorptionCoefficient_Voigt(
        SourceTables=gas,
        Environment={'T':t_upper,'p':1})
    )
    abs_coef_upper.append(hapi.absorptionCoefficient_Voigt(
        SourceTables=gas,
        Environment={'T':t_upper,'p':p_upper/p_ground})
    )
integral_dict = {}
environment = ['Pressure Change', 'Temperature Change', 'Both']
height = ['0km', '10km', 'residual']
fig, ax = plt.subplots(len(main_ghg)*3,3, sharex=False, figsize=(15,20))
fig.set_tight_layout(False)
fig.suptitle('Environmental Factor Comparison',y =0.96)
fig.supxlabel('Wavenumber $(cm^{-1})$')
fig.supylabel('Absorbtion Coeficient $(cm^2/molecule)$') 
plt.subplots_adjust(hspace=1)
plt.ticklabel_format(axis='y',style='sci')
black = colours.durham.ink

for j, abs in enumerate([abs_coef_p_upper, abs_coef_t_upper, abs_coef_upper]):
    for i, (ground, _upper) in enumerate(zip(abs_coef_ground, abs)):
        nu_g, coef_g = ground
        nu_t, coef_t = _upper
        residual = coef_g - coef_t
        # Calculate integrals and add values to dict 
        for k, intergrand in enumerate([coef_g, coef_t]):
            integral = simpson(intergrand,nu_g)
            integral_dict.update({environment[j]+main_ghg[i]+height[k]:integral})
        #Find largest peak in absorbtion spectra for each gas
        max_pos = np.argmax(coef_g)
        half_size = 50
        max_slice = slice(max_pos-half_size,max_pos+half_size)
        #Plotting
        ax[i*3,j].plot(nu_g[max_slice], coef_g[max_slice], c=black)
        ax[i*3+1,j].plot(nu_t[max_slice],coef_t[max_slice], c=black)
        ax[i*3+2,j].plot(nu_g[max_slice], residual[max_slice], c=black)
        ax[i*3,0].set_ylabel('$0km$')
        ax[i*3+1,0].set_ylabel('$30km$')
        ax[i*3+2,0].set_ylabel('$residual$')
    ax[0,j].set_title(environment[j])
    for i, gas in enumerate(main_ghg):
        if i !=0:
            ax[i*3,1].set_title(gas)
        else:
            ax[i*3+1,1].set_title(gas))