Plot.device='/null'
Plot.xAxis='keV'
Plot('ldata')

energies = Plot.x()
edeltas = Plot.xErr()
rates = Plot.y()
errors = Plot.yErr()

labels = Plot.labels()