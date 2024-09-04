resid_lim = 1.5
r = np.linspace(-resid_lim, resid_lim, 1000)

fig = plt.figure(figsize=(6,5), dpi=100)
ax = fig.add_axes((0.1,0.1,0.9,0.9))

for i in range(len(sigma_values)):
    Pr = gauss(r, A_values[i], B_values[i])
    ax.plot(r, Pr, label=sort_order[i], zorder=i, c=plot_colors[i])

ax.set_xlabel('Residual', fontsize=14)
ax.set_ylabel('Probability', fontsize=14)
ax.set_ylim(0, 0.3)

ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.tick_params(axis='x',which='major',direction='in', length=6,width=1.5,color='k',pad=6, labelsize=12,labelcolor='k')
ax.tick_params(axis='x',which='minor',direction='in', length=3,width=1.0,color='k',pad=6, labelsize=12,labelcolor='k')

ax.yaxis.set_major_locator(MultipleLocator(0.05))
ax.yaxis.set_minor_locator(MultipleLocator(0.01))
ax.tick_params(axis='y',which='major',direction='in', length=6,width=1.5,color='k',pad=6, labelsize=12,labelcolor='k')
ax.tick_params(axis='y',which='minor',direction='in', length=3,width=1.0,color='k',pad=6, labelsize=12,labelcolor='k')

ax.grid(True, which='major', axis='both', alpha=0.4, c='#38b000')
ax.grid(True, which='minor', axis='both', alpha=0.1, c='#38b000')

plt.legend(loc='best')

op_filename = 'mr-vel-resid-gaussfit_all-obs'

plt.savefig(os.path.join(output_folder, pdf_folder, op_filename)+'.pdf', bbox_inches='tight') 
plt.savefig(os.path.join(output_folder, png_folder, op_filename)+'.png', bbox_inches='tight') 