lc_data_01 = np.array(hdulist01[1].data)
t01 = np.array([row[0] for row in lc_data_01]) * u.second
rate01 = np.array([row[1] for row in lc_data_01]) * u.s**-1
rateError01 = np.array([row[2] for row in lc_data_01]) * u.s**-1

mask01 = ~np.isnan(rate01)    # Masking all array elements with NaN values

t01 = t01[mask01]
rate01 = rate01[mask01]
rateError01 = rateError01[mask01]