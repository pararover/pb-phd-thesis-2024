output_type = 'nicer-lc_200-1000'
output_detail = '_phasefold-bestfit'

fig, axs = plt.subplots(2, 1, figsize=(10, 10), dpi=120, tight_layout=True)

fig.suptitle(source + ' | ' + observatory + ' | ' + band01 + ' phase-folded lightcurve')

axs[0].errorbar(phase01, rate01, rateError01, label='Lomb-Scargle '+r'$\nu=$'+f'{signal_freq[0].to(u.mHz):.3f}, '+r'$P=$'+f'{signal_period[0].to(u.ks):.1f}', fmt='o', alpha=0.75, zorder=1)
axs[0].plot(phase01_fit, rate01_fit, c=sine_cols[0], label='Best-fit: '+r'$A=$'+f'{A_fit[0]:.1f} counts/s, ' +r'$\phi=$'+f'{phi_fit[0]:.2f} rad, ' +r'$C_0=$'+f'{C_0_fit[0]:.1f} counts/s', zorder=3)
axs[0].axhline(y=C_0_fit[0], c='k', ls='--', lw=1.2, alpha=0.75, label=f'Average rate = {C_0_fit[0]:.1f} counts/s', zorder=2)
axs[0].set_xlabel('Phase (rad)')
axs[0].set_ylabel('Rate (counts/s)')
axs[0].set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], labels=[r'$0$', r'$\dfrac{\pi}{2}$', r'$\pi$', r'$\dfrac{3\pi}{2}$', r'$2\pi$'])
axs[0].legend(loc="lower left")
axs[0].grid()

axs[1].errorbar(phase02, rate01, rateError01, label='Lomb-Scargle '+r'$\nu=$'+f'{signal_freq[1].to(u.mHz):.3f}, '+r'$P=$'+f'{signal_period[1].to(u.ks):.1f}', fmt='o', alpha=0.8)
axs[1].plot(phase02_fit, rate02_fit, c=sine_cols[1], label='Best-fit: '+r'$A=$'+f'{A_fit[1]:.1f} counts/s, ' +r'$\phi=$'+f'{phi_fit[1]:.2f} rad, ' +r'$C_0=$'+f'{C_0_fit[1]:.1f} counts/s', zorder=3)
axs[1].axhline(y=C_0_fit[1], c='k', ls='--', lw=1.2, alpha=0.75, label=f'Average rate = {C_0_fit[1]:.1f} counts/s', zorder=2)
axs[1].set_xlabel('Phase (rad)')
axs[1].set_ylabel('Rate (counts/s)')
#axs[1].set_xlim(0, 2*np.pi)
axs[1].set_xticks([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], labels=[r'$0$', r'$\dfrac{\pi}{2}$', r'$\pi$', r'$\dfrac{3\pi}{2}$', r'$2\pi$'])
axs[1].legend(loc="lower left")
axs[1].grid()

print('Freq.(Hz)\tA (cts/s)\t$\phi$ (rad)\t$C_0$(cts/s)')
for i in range(len(signal_freq)):
  print(str(signal_freq[i].value)+'\t'+str(A_fit[i])+'\t'+str(phi_fit[i])+'\t'+str(C_0_fit[i]))

print(get_output_path(op_path, output_basename, output_type, output_detail))
plt.savefig(get_output_path(op_path, output_basename, output_type, output_detail), dpi=120)