from pysas.wrapper import Wrapper as w

os.environ['SAS_ODF'] = odf_dir
t = w('sasver', [])
t.run()