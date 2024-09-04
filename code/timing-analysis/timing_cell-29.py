output_type = 'nicer-lc_200-1000'
output_detail = '_bestfit'

plt.figure(figsize=(10, 4), dpi=120)
plt.errorbar(t01.to(u.ks), rate01, rateError01, label=band01, fmt='.', alpha=0.75, zorder=1)
plt.plot(T*u.ks/1E3, rate01_fit, c=sine_cols[0], alpha=0.75, label=r'$\nu=$'+f'{signal_freq[0].to(u.mHz):.3f}, '+r'$P=$'+f'{signal_period[0].to(u.ks):.1f}', zorder=2)
plt.plot(T*u.ks/1E3, rate02_fit, c=sine_cols[1], alpha=0.75, label=r'$\nu=$'+f'{signal_freq[1].to(u.mHz):.3f}, '+r'$P=$'+f'{signal_period[1].to(u.ks):.1f}', zorder=3)
plt.xlabel(f"Time ({t01[0].to(u.ks).unit})")
plt.ylabel(f"Rate (counts/{t01[0].unit})")
plt.legend(loc='lower left', fontsize=10)
plt.grid()

plt.title(source + ' | ' + observatory + ' | ' + band01 + ' lightcurve with best-fit sinusoids')

print(get_output_path(op_path, output_basename, output_type, output_detail))
plt.savefig(get_output_path(op_path, output_basename, output_type, output_detail), dpi=120)