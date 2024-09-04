hdu_list = fits.open(srcevt_file)

value_ONTIME = hdu_list['EVENTS'].header['ONTIME']
print(value_ONTIME)