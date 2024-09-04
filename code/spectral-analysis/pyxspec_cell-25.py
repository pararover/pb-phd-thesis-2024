Xset.chatter = 10
Fit.renorm(setting='auto')
Fit.perform()

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