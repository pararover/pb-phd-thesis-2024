sas_task = "evselect" # SAS task to be executed                  

# Arguments of SAS Command
filter_expression = f'{pn_qflag} && (PATTERN=={pn_pattern}) && (FLAG=={pn_flag})'
inargs     = [f'table={pn_dir}/{pnevt_list[0]}', 'keepfilteroutput=yes', 'withfilteredset=yes',f'filteredset={filt_file}', 'writedss=yes', 'updateexposure=yes', 'filterexposure=yes', 'energycolumn=PHA', f'expression={filter_expression}']
print(f'Filter expression to use: {filter_expression} \n')
print(f'SAS command to be executed: {sas_task}, with arguments: \n')
inargs