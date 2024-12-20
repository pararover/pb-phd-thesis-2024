idx = T01.value.argsort()
params, covariance = curve_fit(lambda t01, A, phi, C_0: sinusoid(t01, signal_freq[0].value, A, phi, C_0), T01.value[idx], rate01.value[idx], p0=initial_guess)
A_fit.append(params[0])
phi_fit.append(params[1])
C_0_fit.append(params[2])

idx = T02.value.argsort()
params, covariance = curve_fit(lambda t01, A, phi, C_0: sinusoid(t01, signal_freq[1].value, A, phi, C_0), T02.value[idx], rate01.value[idx], p0=initial_guess)
A_fit.append(params[0])
phi_fit.append(params[1])
C_0_fit.append(params[2])