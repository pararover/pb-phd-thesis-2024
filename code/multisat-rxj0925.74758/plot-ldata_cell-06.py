energy_lo = 0.2
energy_hi = 1.0
for file in ldata_files:
    data = np.loadtxt(file, skiprows=3)
    plot_ldata(data,
               os.path.basename(file),
               (os.path.join(output_folder, pdf_folder), os.path.join(output_folder, png_folder)), # To be modified while on Google Colab
               energy_lo=energy_lo, energy_hi=energy_hi)