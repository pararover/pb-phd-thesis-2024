sas_task = "backscale" # SAS task to be executed                  

# Arguments of SAS Command
inargs = [f'spectrumset={pn_dir}/{srcspec_file}', f'badpixlocation={pn_dir}/{pnevt_list[0]}']

print(f'SAS command to be executed: {sas_task}, with arguments: \n')
inargs