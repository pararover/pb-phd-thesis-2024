output_type = 'nicer-ls'
output_detail = '_bothbands-inset'

signal_freq = []
signal_period = []
signal_power01, signal_power02 = [], []

fig, ax1 = plt.subplots(figsize=(10, 4), dpi=120)

ax1.plot(frequency01.to(u.mHz), power01, c='r', alpha=0.8, label=band01, zorder=1)
ax1.plot(frequency02.to(u.mHz), power02, c='b', alpha=0.8, label=band02, zorder=2)
ax1.set_xlim(-0.5, 1.5)
ax1.set_ylim(-0.1, 0.6)
ax1.set_xticks([0.0, 0.5, 1.0, 1.5],[0.0, 0.5, 1.0, 1.5])
ax1.set_xlabel('Frequency (mHz)')
ax1.set_ylabel('Power / Frequency')
ax1.set_title(source + ' | ' + observatory + ' | Lomb-Scargle periodogram')
ax1.legend(loc="lower left")
ax1.grid()

x1, x2, y1, y2 = 0.0, 0.1, -0.05, 0.55  # subregion of the original image
axins = ax1.inset_axes([0.58, 0.58, 0.39, 0.38], xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])
axins.plot(frequency01.to(u.mHz), power01, c='r', alpha=0.8, zorder=1)
axins.plot(frequency02.to(u.mHz), power02, c='b', alpha=0.8, zorder=2)

idx=5;  axins.axvline(x=frequency01[idx].to(u.mHz).value, c='g', alpha=1.0, ls='--', lw=1, label=f'{frequency01[idx].to(u.mHz).value:.3f} mHz')
signal_freq.append(frequency01[idx])
signal_period.append(1/frequency01[idx])
signal_power01.append(power01[idx])
signal_power02.append(power02[idx])

idx=10; axins.axvline(x=frequency01[idx].to(u.mHz).value, c='m', alpha=1.0, ls='--', lw=1, label=f'{frequency01[idx].to(u.mHz).value:.3f} mHz')
signal_freq.append(frequency01[idx])
signal_period.append(1/frequency01[idx])
signal_power01.append(power01[idx])
signal_power02.append(power02[idx])

axins.set_xticks(np.arange(0, 0.11, 0.02), np.arange(0, 0.11, 0.02))
axins.set_yticks([0.0, 0.25, 0.50], [0.0, 0.25, 0.50])
axins.legend()
axins.grid()

ax1.indicate_inset_zoom(axins, edgecolor="black")

print('Freq.(Hz)\tPeriod(s)\tPower/Freq (01)\tPower/Freq (02)')
for i in range(len(signal_freq)):
  print(str(signal_freq[i].value)+'\t'+str(signal_period[i].value)
  +'\t'+str(signal_power01[i].value)+'\t'+str(signal_power02[i].value))

print(get_output_path(op_path, output_basename, output_type, output_detail))
plt.savefig(get_output_path(op_path, output_basename, output_type, output_detail), dpi=120)