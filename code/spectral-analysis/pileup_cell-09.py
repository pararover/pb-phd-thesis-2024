src_coord_file = 'src.xy'
with open(src_coord_file, 'w+') as f:
    for i in range(len(src_reg)-1):
        f.write('%f\n' %src_reg[i])
    print(f"Source region successfully saved in file {src_coord_file}!")
f.close()

srcevt_file = f'{source_name}_filt_{int(px_to_arcsec(src_reg[2]))}arcsec.fits'