# Run this cell if rebinning is required during a later session
from astroda_utilities import *

source_name  = 'rx-j0925.7-4758'
dataset_name = 'parag-dataset'

obs_id       = get_obsid()
odf_dir, work_dir, epic_dir, mos_dir, pn_dir, rgs_dir = get_dirs(source_name, dataset_name)
os.chdir(odf_dir)
rev = get_rev()

os.environ['SAS_CCF'] = f'{odf_dir}/ccf.cif'
os.environ['SAS_ODF'] = f'{odf_dir}/{rev}_{obs_id}_SCX00000SUM.SAS'

t = w('sasver', [])
t.run()

os.chdir(pn_dir)

srcspec_file = f'{source_name}.src'
bkgspec_file = f'{source_name}.bkg'
rmf_file = f'{source_name}.rmf'
arf_file = f'{source_name}.arf'