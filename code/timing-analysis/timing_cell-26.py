T01_fit = np.linspace(min(T01.value), max(T01.value), 100)
phase01_fit = np.linspace(0, 2*np.pi, 100)
rate01_fit = sinusoid(T01_fit, signal_freq[0].value, A_fit[0], phi_fit[0], C_0_fit[0])

T02_fit = np.linspace(min(T02.value), max(T02.value), 100)
phase02_fit = np.linspace(0, 2*np.pi, 100)
rate02_fit = sinusoid(T02_fit, signal_freq[1].value, A_fit[1], phi_fit[1], C_0_fit[1])