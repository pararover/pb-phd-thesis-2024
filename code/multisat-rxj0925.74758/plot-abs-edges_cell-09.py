energy_lo, energy_hi = 0.3, 1.0
group_plot = group_plots_labels(eufspec_keV_files, obs_dates)

fig = plt.figure(figsize=(8,3), dpi=100)
ax = fig.add_axes((0.1,0.1,0.9,0.9))

for val in sort_order:
    data = np.loadtxt(group_plot[val][0], skiprows=3)
    energy     = data[:,0]
    eufspec    = data[:,4]
    ax.step(energy, eufspec, c=plot_colors[sort_order.index(val)], where='mid', zorder=sort_order.index(val), label=group_plot[val][1])

ax.set_yscale('log')
ax.set_xlabel(r'Energy (keV)', fontsize=14)
ax.set_ylabel(r'Flux density (Photons s$^{-1}$ cm$^{-2}$ keV$^{-1}$)', fontsize=12.2)
ax.set_xlim(energy_lo, energy_hi)
ax.set_ylim(1E-11, 1E-1)

ax.xaxis.set_major_locator(MultipleLocator(0.1))
ax.xaxis.set_minor_locator(MultipleLocator(0.02))
ax.tick_params(axis='x',which='major',direction='in', length=6,width=1.5,color='k',pad=6, labelsize=12,labelcolor='k')
ax.tick_params(axis='x',which='minor',direction='in', length=3,width=1.0,color='k',pad=6, labelsize=12,labelcolor='k')

ax.yaxis.set_major_locator(LogLocator(base=10))
ax.yaxis.set_minor_locator(LogLocator(base=10,subs=(0.2,0.4,0.6,0.8),numticks=12))
ax.yaxis.set_major_formatter(FuncFormatter(log_formatter))
ax.tick_params(axis='y',which='major',direction='in', length=6,width=1.5,color='k',pad=6, labelsize=12,labelcolor='k')
ax.tick_params(axis='y',which='minor',direction='in', length=3,width=1.0,color='k',pad=6, labelsize=12,labelcolor='k')

ax.grid(True, which='major', axis='both', alpha=0.4, c='#38b000')
ax.grid(True, which='minor', axis='both', alpha=0.1, c='#38b000')

ax.legend(loc='lower right')

op_filename = 'mr-vel-uf-keV_abs-edge'

plt.savefig(os.path.join(output_folder, pdf_folder, op_filename)+'.pdf', bbox_inches='tight') # To be modified while on Google Colab
plt.savefig(os.path.join(output_folder, png_folder, op_filename)+'.png', bbox_inches='tight') # To be modified while on Google Colab