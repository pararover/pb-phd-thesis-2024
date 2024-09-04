sas_task = "evselect" # SAS task to be executed                  

# Arguments of SAS Command
inargs     = [f'table={pn_dir}/{filt_file}', 'withimageset=yes', f'imageset={filtimg_file}', 'xcolumn=X', 'ycolumn=Y']
print(f'SAS command to be executed: {sas_task}, with arguments: \n')
inargs