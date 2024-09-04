# Extracting log g values from the NLTE filenames
files = os.listdir(pureH_dir)
files.sort()
logg_values = []
nlte_files = {}
for f in files:
    logg_values.append(find_float(f))
    nlte_files.update({find_float(f):f})