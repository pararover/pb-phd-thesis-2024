output_type = 'lc'
output_detail = ''

plt.figure(figsize=(10, 4), dpi=120)
plt.errorbar(t01.to(u.ks), rate01, yerr=rateError01, fmt='b.', alpha=0.5, label=band01)
plt.errorbar(t02.to(u.ks), rate02, yerr=rateError02, fmt='r.', alpha=0.5, label=band02)
plt.xlabel(f"Time ({t01.to(u.ks)[0].unit})")
plt.ylabel(f"Rate (counts/{t01[0].unit})")
plt.title(source + ' | ' + observatory + ' lightcurve')
plt.legend()
plt.grid()

plt.savefig(get_output_path(op_path, output_basename, output_type, output_detail), dpi=120)