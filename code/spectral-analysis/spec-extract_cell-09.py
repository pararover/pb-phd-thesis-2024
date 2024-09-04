filtimg_file = f'{source_name}_filt-img.fits'

sas_task = "ebkgreg" # SAS task to be executed

# Arguments of SAS Command
inargs     = [f'imageset={pn_dir}/{filtimg_file}', 'withsrclist=no', 'withcoords=yes', 'coordtype=EQPOS', f'x={x}', f'y={y}', f'r={r}']
print(f'SAS command to be executed: {sas_task}, with arguments: \n')
inargs