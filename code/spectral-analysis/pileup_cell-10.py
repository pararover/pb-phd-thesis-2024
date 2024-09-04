sas_task = "evselect" # SAS task to be executed                  

# Arguments of SAS Command
filter_expression = f'(X,Y) IN circle({src_reg[0]},{src_reg[1]},{src_reg[2]})'
inargs     = [f'table={pn_dir}/{filt_file}', 'keepfilteroutput=yes', 'withfilteredset=yes', f'filteredset={srcevt_file}', f'expression={filter_expression}']
print(f'Filter expression to use: {filter_expression} \n')
print(f'SAS command to be executed: {sas_task}, with arguments: \n')
inargs