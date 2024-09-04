min_counts = 10
grp_file = source_name + f'_{min_counts:02d}c.grp'

sas_task = "specgroup" # SAS task to be executed                  

# Arguments of SAS Command
inargs = [f'mincounts={min_counts}', f'spectrumset={pn_dir}/{srcspec_file}', f'rmfset={pn_dir}/{rmf_file}', f'arfset={pn_dir}/{arf_file}', f'backgndset={pn_dir}/{bkgspec_file}', f'groupedset={grp_file}']

print(f'SAS command to be executed: {sas_task}, with arguments: \n')
inargs