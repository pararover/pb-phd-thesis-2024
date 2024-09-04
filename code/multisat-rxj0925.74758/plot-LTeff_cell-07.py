plot_colors = ['#c9184a', '#007200', '#f46036', '#1d3557', '#7209b7', '#1982c4']
plot_markers = ["o", "^", "s", "*", "X", "d"]
plot_markersize = [150, 150, 150, 180, 150, 150]
plot_labels = ["1994-12-22 | ASCA:SIS1",
               "2000-11-14 | Chandra:ACIS",
               "2000-12-16 | XMM:EPIC-pn",
               "2019-05-18 | NICER:XTI",
               "2019-05-19 | NICER:XTI",
               "2019-05-19 | NICER:XTI"]

fig = plt.figure(figsize=(6,4), dpi=100)
ax = fig.add_axes((0.1,0.1,0.9,0.9))

for i in range(len(T)):
  ax.errorbar(T[i], L[i], xerr = [np.array([T_errmin[i]]), np.array([T_errmax[i]])], yerr = [np.array([L_errmin[i]]), np.array([L_errmax[i]])], fmt='.', c=plot_colors[i], alpha=0.8)
  ax.scatter(T[i], L[i], c=plot_colors[i], marker=plot_markers[i], s=plot_markersize[i], label=plot_labels[i])
ax.set_yscale('log')
ax.set_xlim(150, 50)
ax.set_ylim(1E0,1E3)
ax.set_xlabel(r"$T_\mathrm{eff}$ (kK)", fontsize=14)
ax.set_ylabel(r"$L_*$ ($\times 10^{"+f"{common_pow}"+"}$ erg s$^{-1}$)", fontsize=14)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(2))
ax.tick_params(axis='x',which='major',direction='in', length=6,width=1.5,color='k',pad=6, labelsize=12,labelcolor='k')
ax.tick_params(axis='x',which='minor',direction='in', length=3,width=1.0,color='k',pad=6, labelsize=12,labelcolor='k')

ax.yaxis.set_major_locator(LogLocator(base=10))
ax.yaxis.set_minor_locator(LogLocator(base=10,subs=(0.2,0.4,0.6,0.8,1.0),numticks=12))
ax.yaxis.set_major_formatter(FuncFormatter(log_formatter))
ax.tick_params(axis='y',which='major',direction='in', length=6,width=1.5,color='k',pad=6, labelsize=12,labelcolor='k')
ax.tick_params(axis='y',which='minor',direction='in', length=3,width=1.0,color='k',pad=6, labelsize=12,labelcolor='k')
ax.grid(True, which='major', axis='both', alpha=0.4, c='#38b000')
ax.grid(True, which='minor', axis='both', alpha=0.1, c='#38b000')

ax.legend(loc="lower right")

plt.savefig('L-Teff_all-obs.pdf', bbox_inches='tight')
plt.savefig('L-Teff_all-obs.png', bbox_inches='tight')