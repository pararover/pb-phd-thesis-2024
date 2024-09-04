lc_data_02 = np.array(hdulist02[1].data)
t02 = np.array([row[0] for row in lc_data_02]) * u.second
rate02 = np.array([row[1] for row in lc_data_02]) * u.s**-1
rateError02 = np.array([row[2] for row in lc_data_02]) * u.s**-1

mask02 = ~np.isnan(rate02)    # Masking all array elements with NaN values

t02 = t02[mask02]
rate02 = rate02[mask02]
rateError02 = rateError02[mask02]