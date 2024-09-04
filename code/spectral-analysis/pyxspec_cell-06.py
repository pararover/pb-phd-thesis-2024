modelstats_df = pd.DataFrame(columns=['additive_model', 'log_g', 'reduced_chisq', 'T_eff'])
os.mkdir(os.path.join(pn_dir, 'fits'))
os.mkdir(os.path.join(pn_dir, 'resids'))