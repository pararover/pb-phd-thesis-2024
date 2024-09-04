# https://heasarc.gsfc.nasa.gov/lheasoft/heasoftpy/
import heasoftpy as hsp

fstat = hsp.fstatistic(infile=srcevt_file, colname='PHA', rows='-')
total_counts = fstat.params['numb']
print(total_counts)