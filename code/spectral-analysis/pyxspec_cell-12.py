print(f'Reduced Chi-squared: {reduced_chisq(Fit)}')

T_bb = keV_to_K(model1.bbody.kT.values[0])
print(f'Best-fit blackbody temperature: {display_temp(T_bb)[0]} {display_temp(T_bb)[1]}')