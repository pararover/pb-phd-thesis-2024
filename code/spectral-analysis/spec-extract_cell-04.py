src_reg = []
f = open('src.xy', 'r')
for x in f.readlines():
    src_reg.append(float(x))
f.close()
src_reg.append(arcsec_to_px(float(input("Enter radius of source region (in arcsec): "))))
print(src_reg)