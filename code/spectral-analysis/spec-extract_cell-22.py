rmf_file = f'{source_name}.rmf'

sas_task = "rmfgen" # SAS task to be executed                  

# Arguments of SAS Command
inargs = [f'spectrumset={pn_dir}/{srcspec_file}', f'rmfset={rmf_file}']

print(f'SAS command to be executed: {sas_task}, with arguments: \n')
inargs