bkg_reg = []
f = open('bkg.reg', 'r')
for x in f.readlines():
    bkg_reg.append(float(x))
f.close()