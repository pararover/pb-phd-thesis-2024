idx = 2

fig = plt.figure(figsize=(8,3), dpi=100)
ax = fig.add_axes((0.1,0.1,0.9,0.9))

op_filename = plot_edge_overlay('mr-vel', idx, 'all', (wave_lo, wave_hi), ax, group_plot, sort_order, temp_df, flux_lo=1E-22, flux_hi=1E-11, text_yposn=0.4)

ax.xaxis.set_major_locator(MultipleLocator(2.0))
ax.xaxis.set_minor_locator(MultipleLocator(0.2))

plt.savefig(os.path.join(output_folder, pdf_folder, op_filename)+'.pdf', bbox_inches='tight')
plt.savefig(os.path.join(output_folder, png_folder, op_filename)+'.png', bbox_inches='tight')