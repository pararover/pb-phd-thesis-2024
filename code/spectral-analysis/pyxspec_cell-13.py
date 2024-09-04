model1.show()

bbody_kT = float(input("Enter bbody.kT (in keV): "))
model1.bbody.kT = bbody_kT
model1.bbody.kT.frozen = False