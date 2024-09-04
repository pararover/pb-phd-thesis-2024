idx = 2
elem_list = ['Ne']

fig = plt.figure(figsize=(6,4), dpi=100)
ax = fig.add_axes((0.1,0.1,0.9,0.9))

op_filename = plot_edge_overlay('mr-vel', idx, elem_list, (12.5, 16), ax, group_plot, sort_order, edge_df[edge_df['element'].isin(elem_list)], flux_lo=4E-13, flux_hi=2E-12, text_yposn=0.94)

ax.xaxis.set_major_locator(MultipleLocator(1.0))
ax.xaxis.set_minor_locator(MultipleLocator(0.1))

ax.legend(loc='best', fontsize=12)

plt.savefig(os.path.join(output_folder, pdf_folder, op_filename)+'.pdf', bbox_inches='tight')
plt.savefig(os.path.join(output_folder, png_folder, op_filename)+'.png', bbox_inches='tight')