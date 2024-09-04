sas_task = "evselect" # SAS task to be executed                  

# Arguments of SAS Command
inargs     = [f'table={pn_dir}/{srcevt_file}', 'withimageset=yes', f'imageset={srcimg_file}', 'xcolumn=X', 'ycolumn=Y', f'expression={filter_expression}']
print(f'SAS command to be executed: {sas_task}, with arguments: \n')
inargs