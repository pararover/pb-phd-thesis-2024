src_reg_file = 'src.reg'
with open(src_reg_file, 'w+') as f:
    for i in range(len(src_reg)):
        f.write('%f\n' %src_reg[i])
    print(f"Source region successfully saved in file {src_reg_file}!")
f.close()