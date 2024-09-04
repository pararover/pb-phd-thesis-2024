from astroda_utilities import *

source_name  = 'rx-j0925.7-4758'
dataset_name = 'parag-dataset'

obs_id       = get_obsid()
odf_dir, work_dir, epic_dir, mos_dir, pn_dir, rgs_dir = get_dirs(source_name, dataset_name)
os.chdir(odf_dir)
rev = get_rev()