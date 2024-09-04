idx = 5
data = np.loadtxt(group_plot[sort_order[idx]][0], skiprows=3)
resid   = data[:,2]

sns.set_style('ticks')
fig, ax = plt.subplots(figsize=(6,5), dpi=100)

hist = sns.histplot(resid, kde=True, bins=10,#'doane',
                    color='#4e148c', stat='probability',
                    ax=ax, alpha=0.65, line_kws={'label': "KDE fit"})
# Ref: https://stats.stackexchange.com/questions/798/calculating-optimal-number-of-bins-in-a-histogram

resid_values = hist.get_lines()[0].get_data()[0]
kde_values = hist.get_lines()[0].get_data()[1]
(A, B), covariance = curve_fit(gauss, resid_values, kde_values)
sigma = 1 / np.sqrt(2*B)

ax.plot(resid_values, gauss(resid_values, A, B), c='#c32f27', label=r'Gauss. fit: $\sigma=$'+f'{sigma:.3f}')

ax.set_xlabel('Residual', fontsize=14)
ax.set_ylabel('Probability', fontsize=14)

ax.tick_params(axis='x',which='major',direction='in',
                   length=6,width=1.5,color='k',pad=6,
                   labelsize=12,labelcolor='k')

ax.set_ylim(0, 0.4)
hist_lim = max([abs(min(resid)), abs(max(resid))])
ax.set_xlim(-(round(hist_lim, 1)*1.1), (round(hist_lim, 1)*1.1))

ax.grid(True, which='major', axis='both', alpha=0.4, c='#8f857d', lw=0.7)

plt.legend(loc='upper right', fontsize=10)

data_file = os.path.basename(group_plot[sort_order[idx]][0])

print(os.path.join(output_folder, pdf_folder, data_file)[:-4]+'-hist.pdf')
print(os.path.join(output_folder, png_folder, data_file)[:-4]+'-hist.png')

plt.savefig(os.path.join(output_folder, pdf_folder, data_file)[:-4]+'-hist.pdf', bbox_inches='tight')
plt.savefig(os.path.join(output_folder, png_folder, data_file)[:-4]+'-hist.png', bbox_inches='tight')