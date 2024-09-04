idx = 5
maj_tick, min_tick = 0.5, 0.1

energy_lo = 0.2
energy_hi = 1.0

data = np.loadtxt(group_plot[sort_order[idx]][0], skiprows=3)
plot_resid(data,os.path.basename(group_plot[sort_order[idx]][0]), (os.path.join(output_folder, pdf_folder), os.path.join(output_folder, png_folder)), energy_lo=energy_lo, energy_hi=energy_hi, major_tick=maj_tick, minor_tick=min_tick)