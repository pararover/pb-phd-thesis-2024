lo_E = 0.2 # keV
hi_E = 1.1 # keV

ignore_string = f'**-{lo_E} {hi_E}-**'
data.ignore(ignore_string)