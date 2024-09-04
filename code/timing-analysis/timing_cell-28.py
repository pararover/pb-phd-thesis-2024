T = np.linspace(min(t01.value), max(t01.value), 1000)
rate01_fit = sinusoid(T, signal_freq[0].value, A_fit[0], phi_fit[0], C_0_fit[0])
rate02_fit = sinusoid(T, signal_freq[1].value, A_fit[1], phi_fit[1], C_0_fit[1])