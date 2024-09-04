import seaborn as sns
from scipy.stats import norm

resid_hist = sns.displot(x=residuals, bins=20, kde=True)
resid_hist.set(title=f'{source_name.upper()} $|$ {obs_id} $|$ Model: {mod_1} $|$ Residual Histogram')
kde_curve = resid_hist.ax.lines[0].get_ydata()

mu, std = norm.fit(residuals)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)

scale_factor = max(kde_curve) / (1 / (std * np.sqrt(2 * np.pi)))
p_scaled = p * scale_factor

plt.plot(x, p_scaled, 'r', linewidth=2)
plt.xlabel(f'Residual ({Plot.labels(plotWindow=2)[1]})')
plt.ylabel('Counts')
plt.savefig(f'{pn_dir}/resids/{source_name}-{obs_id}_{comp_add}_resid-dist.png', dpi=200)