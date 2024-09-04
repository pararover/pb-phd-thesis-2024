# Clear all data and models
AllModels.clear()  # Clear all models
AllData.clear()    # Clear all data

# Load the group spectral file
grp_file = find_specgroup_file(min_counts=10)
data = Spectrum(f'{pn_dir}/{grp_file}')  # load spectra grouped file