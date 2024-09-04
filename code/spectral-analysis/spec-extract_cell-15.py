bkgspec_file = f'{source_name}.bkg'

filt_file = f'{source_name}_filt.fits'
bin_size = 5
pattern = 'PATTERN==0'

sas_task = "evselect" # SAS task to be executed

# Arguments of SAS Command
filter_expression = f'({pattern}) && ((X,Y) IN circle({bkg_reg[0]},{bkg_reg[1]},{bkg_reg[2]}))'
inargs     = [f'table={pn_dir}/{filt_file}', 'withspectrumset=yes', f'spectrumset={bkgspec_file}', 'energycolumn=PI', f'spectralbinsize={bin_size}', 'withspecranges=yes','specchannelmin=0', 'specchannelmax=20479', f'expression={filter_expression}']
print(f'Filter expression to use: {filter_expression} \n')
print(f'SAS command to be executed: {sas_task}, with arguments: \n')
inargs