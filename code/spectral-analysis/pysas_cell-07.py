os.environ['SAS_ODF'] = f'{odf_dir}/{rev}_{obs_id}_SCX00000SUM.SAS'
t = w('sasver', [])
t.run()