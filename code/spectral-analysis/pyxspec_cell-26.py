matplotlib.rcParams['text.usetex'] = True
fig, ax = plt.subplots(2, 1, figsize=(6,6), dpi=150)
fig.suptitle(f'{source_name.upper()} $|$ {obs_id} $|$ Model: {nlte_type}(log g={logg})*vphabs*tbabs')

ax[0].errorbar(energies, rates, xerr=edeltas, yerr=errors, fmt='.', ms=3, elinewidth=1.0, label='Data')
ax[0].step(energies, foldedmodel, where='mid', c='r', label='Model')
ax[0].set_ylabel(Plot.labels(plotWindow=1)[1])
ax[0].set_xscale('linear')
ax[0].set_yscale('log')
ax[0].grid()
ax[0].ticklabel_format(axis='x', style='plain')
ax[0].set_title(f"Data and folded model $|\,\chi^2=${reduced_chisq(Fit)}", fontsize=10)
ax[0].legend(loc='best')

ax[1].axhline(0, c='k', lw=0.8)
ax[1].errorbar(energies, residuals, xerr=edeltas, yerr=errors, fmt='.', ms=4, elinewidth=1.0)
ax[1].set_xlabel(Plot.labels(plotWindow=2)[0])
ax[1].set_ylabel(Plot.labels(plotWindow=2)[1])
ax[1].set_title("Residuals", fontsize=10)
ax[1].grid()

plt.savefig(f'{pn_dir}/fits/{source_name}-{obs_id}_pureH-{logg}_specfit.png', dpi=200)