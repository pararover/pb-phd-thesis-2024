group_plot = group_plots_labels(eufspec_files, obs_dates)
sort_order = list(obs_dates.keys())

fig = plt.figure(figsize=(6,5), dpi=100)
ax = fig.add_axes((0.1,0.1,0.9,0.9))

for val in sort_order:
    data = np.loadtxt(group_plot[val][0], skiprows=3)
    wavelength = data[:,0]
    eufspec    = data[:,4]
    ax.step(wavelength, eufspec, c=plot_colors[sort_order.index(val)],
             where='mid', zorder=sort_order.index(val), label=group_plot[val][1])

ax.set_yscale('log')
ax.set_xlabel(r'Wavelength $\lambda$ ($\AA$)', fontsize=14)
ax.set_ylabel(r'Flux density $F_\lambda$ (erg s$^{-1}$ cm$^{-2}$ $\AA^{-1}$)', fontsize=14)
ax.set_xlim(wave_lo, wave_hi)
#ax.set_ylim(1E-22, 1E-12)

ax.xaxis.set_major_locator(MultipleLocator(2.0))
ax.xaxis.set_minor_locator(MultipleLocator(1.0))
ax.tick_params(axis='x',which='major',direction='in',
               length=6,width=1.5,color='k',pad=6,
               labelsize=12,labelcolor='k')
ax.tick_params(axis='x',which='minor',direction='in',
               length=3,width=1.0,color='k',pad=6,
               labelsize=12,labelcolor='k')

ax.yaxis.set_major_locator(LogLocator(base=10))
ax.yaxis.set_minor_locator(LogLocator(base=10,subs=(0.2,0.4,0.6,0.8),numticks=12))
ax.yaxis.set_major_formatter(FuncFormatter(log_formatter))
ax.tick_params(axis='y',which='major',direction='in',
               length=6,width=1.5,color='k',pad=6,
               labelsize=12,labelcolor='k')
ax.tick_params(axis='y',which='minor',direction='in',
               length=3,width=1.0,color='k',pad=6,
               labelsize=12,labelcolor='k')

ax.grid(True, which='major', axis='both', alpha=0.4, c='#38b000')
ax.grid(True, which='minor', axis='both', alpha=0.1, c='#38b000')

ax.legend(loc='lower left')

op_filename = 'mr-vel-uf_all-obs'
#op_filename = 'mr-vel-uf_all-obs_12-24'
#op_filename = 'mr-vel-uf_all-obs_24-36'

plt.savefig(os.path.join(output_folder, pdf_folder, op_filename)+'.pdf', bbox_inches='tight') # To be modified while on Google Colab
plt.savefig(os.path.join(output_folder, png_folder, op_filename)+'.png', bbox_inches='tight') # To be modified while on Google Colab