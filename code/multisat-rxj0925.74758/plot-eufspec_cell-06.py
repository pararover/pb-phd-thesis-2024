wave_lo = 12.0
wave_hi = 42.0
for file in eufspec_files:
    data = np.loadtxt(file, skiprows=3)
    plot_eufspec(data,
               os.path.basename(file),
               (os.path.join(output_folder, pdf_folder), os.path.join(output_folder, png_folder)), # To be modified while on Google Colab
               wave_lo=wave_lo, wave_hi=wave_hi)