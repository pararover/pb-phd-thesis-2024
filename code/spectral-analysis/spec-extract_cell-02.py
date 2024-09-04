rev = get_rev()
os.environ['SAS_CCF'] = f'{odf_dir}/ccf.cif'
os.environ['SAS_ODF'] = f'{odf_dir}/{rev}_{obs_id}_SCX00000SUM.SAS'

t = w('sasver', [])
t.run()