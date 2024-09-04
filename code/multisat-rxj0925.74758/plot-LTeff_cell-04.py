pows = []
for L_list in Luminosity:
  pows.append(fexp(L_list[3].value))
common_pow = min(pows)

L = []
L_errmin, L_errmax = [], []
for L_list in Luminosity:
  L_val = L_list[3].value / (10**common_pow)
  del_L_lo = L_val - L_list[4].value / (10**common_pow)
  del_L_hi = L_list[5].value / (10**common_pow) - L_val
  L.append(L_val)
  L_errmin.append(del_L_lo)
  L_errmax.append(del_L_hi)
L_err = [L_errmin, L_errmax]