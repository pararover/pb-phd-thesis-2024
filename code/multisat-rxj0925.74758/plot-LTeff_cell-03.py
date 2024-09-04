nH_bb = [1.4E22, 3.7E22]
nH_optical = [1.0E22, 1.9E22]
R = 425 * u.parsec

flux_data = np.loadtxt('fluxes.dat', skiprows=1)
log10Flux = flux_data[0:,1:]
Flux = np.power(10, log10Flux) * u.erg / (u.s * (u.cm)**2)
Luminosity = (4 * np.pi * R**2 * Flux).to(u.erg / u.s)