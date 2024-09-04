output_type = 'nicer-lc'
output_detail = '_bothbands-inset'

fig, ax1 = plt.subplots(figsize=(10, 4), dpi=120)

ax1.errorbar(t01.to(u.ks), rate01, yerr=rateError01, fmt='b.', alpha=0.5, label=band01, zorder=2)
ax1.errorbar(t02.to(u.ks), rate02, yerr=rateError02, fmt='r.', alpha=0.5, label=band02, zorder=1)
ax1.set_ylim(6, 30)
ax1.set_xlabel(f"Time ({t01.to(u.ks)[0].unit})")
ax1.set_ylabel(f"Rate (counts/{t01[0].unit})")
ax1.set_title(source + ' | ' + observatory + ' lightcurve')
ax1.legend()
ax1.grid()

x1, x2, y1, y2 = 11, 12.75, 9, 18  # subregion of the original image
axins = ax1.inset_axes(
    [0.58, 0.58, 0.39, 0.38],
    xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])
axins.errorbar(t01.to(u.ks), rate01,
             yerr=rateError01, fmt='b.', alpha=0.8, label=band01, zorder=2)
axins.errorbar(t02.to(u.ks), rate02,
             yerr=rateError02, fmt='r.', alpha=0.6, label=band02, zorder=1)
axins.set_xticks([11, 11.5, 12, 12.5], [11, 11.5, 12, 12.5])
axins.set_yticks([9, 12, 15, 18], [9, 12, 15, 18])
axins.grid()

ax1.indicate_inset_zoom(axins, edgecolor="black")

print(get_output_path(op_path, output_basename, output_type, output_detail))
plt.savefig(get_output_path(op_path, output_basename, output_type, output_detail), dpi=120)