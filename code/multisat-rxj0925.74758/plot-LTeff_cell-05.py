Teff_data = np.loadtxt('teff.dat', skiprows=1)[:,1:]
T = Teff_data[:,0]
T_errmin, T_errmax = Teff_data[:,1], Teff_data[:,2]
T_errmin = T - Teff_data[:,1]
T_errmax = Teff_data[:,2] - T
T_err = [T_errmin, T_errmax]