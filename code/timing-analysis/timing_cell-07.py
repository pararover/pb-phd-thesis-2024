def sinusoid(t, nu, A, phi, C_0):
  C = A * np.sin(2 * np.pi * nu * t + phi) + C_0
  return C

def get_output_path(op_path, output_basename, output_type, output_detail):
  output_fname = output_basename + output_type + output_detail + '.png'
  output_path = os.path.join(op_path, output_fname)
  return output_path