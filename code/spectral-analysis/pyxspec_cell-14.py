Fit.renorm(setting='auto')
Fit.perform()

print(f'Reduced Chi-squared: {reduced_chisq(Fit)}')
T_bb = keV_to_K(model1.bbody.kT.values[0])
print(f'Best-fit blackbody temperature: {display_temp(T_bb)[0]} {display_temp(T_bb)[1]}')

Plot.device='/null'
Plot.xAxis='keV'
Plot('ldata resid')
energies = Plot.x()
edeltas = Plot.xErr()
rates = Plot.y(plotWindow = 1)
errors = Plot.yErr()

foldedmodel = Plot.model()
residuals = Plot.y(plotWindow = 2)

labels = Plot.labels()