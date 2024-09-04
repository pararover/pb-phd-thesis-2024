arf_file = f'{source_name}.arf'

sas_task = "arfgen" # SAS task to be executed                  

print("Checking for Response File ..... \n")
# Check if RESP file is available.
if os.path.isfile(rmf_file):
    print (f"File {rmf_file} exists. \n")
    inargs = [f'spectrumset={pn_dir}/{srcspec_file}', f'arfset={arf_file}', 'withrmfset=yes', f'rmfset={pn_dir}/{rmf_file}', f'badpixlocation={pn_dir}/{pnevt_list[0]}', 'detmaptype=psf']
    print(f'SAS command to be executed: {sas_task}, with arguments: \n')
    print(inargs)
else:
    print (f'File {rmf_file} does not exist, please run the rmfgen task first, or check. \n')