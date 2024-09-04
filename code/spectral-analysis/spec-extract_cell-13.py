bkg_reg_file = 'bkg.reg'
with open(bkg_reg_file, 'w+') as f:
    for i in range(len(bkg_reg)):
        f.write('%f\n' %bkg_reg[i])
    print(f"Background region successfully saved in file {bkg_reg_file}!")
f.close()