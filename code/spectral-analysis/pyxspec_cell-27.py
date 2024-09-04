print(f'Reduced Chi-squared: {reduced_chisq(Fit)}')

T_bb = modl.rauch.T.values[0]
print(f'Best-fit blackbody temperature: {display_temp(T_bb)[0]} {display_temp(T_bb)[1]}')