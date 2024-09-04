import os
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, LogLocator, FormatStrFormatter, MaxNLocator, FuncFormatter
import seaborn as sns
import pandas as pd
from scipy.optimize import curve_fit
from glob import glob
import sys
from astropy import units as u
from astropy import constants as const

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
# mpl.rcParams['font.family'] = 'Carlito'
# mpl.rcParams['font.family'] = 'Liberation Sans'
mpl.rcParams['font.family'] = 'Calibri'

pn_dir = 'pn'
acis_dir = 'ACIS'
sis_dir = 'SIS1'
xti_dir = 'XTI'

def gauss(x, A, B): 
    y = A*np.exp(-1*B*x**2) 
    return y

def log_formatter(x, pos):
    if x == 1:
        return '1'
    else:
        return f'$10^{{{int(np.log10(x))}}}$'

def keV_to_angstrom(keV_list):
  ang_list = []
  temp = ((const.h * const.c)/(keV_list*u.keV)).to(u.Angstrom)
  for i in range(len(temp)):
    ang_list.append(round(temp[i].value, 2))
  return sorted(ang_list)

def keV_to_ang(keV_val, sigfig=3):
  if not keV_val == 0:
    ang_val = ((const.h * const.c)/(keV_val*u.keV)).to(u.Angstrom).value
  else:
    ang_val = np.NaN
  return round(ang_val, sigfig)
  
def ang_to_keV(ang_val, sigfig=3):
  if not ang_val == 0:
    keV_val = ((const.h * const.c)/(ang_val*u.Angstrom)).to(u.keV).value
  else:
    keV_val = np.NaN
  return round(keV_val, sigfig)

def find_files(folder, file_type, file_ext):
    files = []
    all_files = os.listdir(folder)
    for file in all_files:
        if not file.find(file_type)==-1:
            if file.endswith(file_ext):
                files.append(os.path.join(os.path.abspath(file)))
    return files

def plot_ldata(data, data_file, op_folders, energy_lo=0.2, energy_hi=1.0):
    energy = data[:,0]
    ebins  = data[:,1]
    rate   = data[:,2]
    rerr   = data[:,3]
    model  = data[:,4]
    
    fig = plt.figure(figsize=(6,4), dpi=100)
    ax = fig.add_axes((0.1,0.1,0.9,0.9))

    ax.errorbar(energy, rate, xerr=ebins, yerr=rerr, fmt='+', c='#3f37c9', label='Data')
    ax.step(energy, model, c='#ef233c', where='mid', zorder=3, label='Model')
    ax.set_yscale('log')
    ax.set_xlabel(r'Energy (keV)', fontsize=14)
    ax.set_ylabel(r'counts s$^{-1}$ keV$^{-1}$', fontsize=14)
    ax.set_xlim(energy_lo, energy_hi)

    ax.xaxis.set_major_locator(MultipleLocator(0.1))
    ax.xaxis.set_minor_locator(MultipleLocator(0.01))
    ax.tick_params(axis='x',which='major',direction='in',
                   length=6,width=1.5,color='k',pad=6,
                   labelsize=12,labelcolor='k')
    ax.tick_params(axis='x',which='minor',direction='in',
                   length=3,width=1.0,color='k',pad=6,
                   labelsize=12,labelcolor='k')

    ax.yaxis.set_major_locator(LogLocator(base=10))
    ax.yaxis.set_minor_locator(LogLocator(base=10,subs=(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9),numticks=12))
    ax.yaxis.set_major_formatter(FuncFormatter(log_formatter))
    ax.tick_params(axis='y',which='major',direction='in',
                   length=6,width=1.5,color='k',pad=6,
                   labelsize=12,labelcolor='k')
    ax.tick_params(axis='y',which='minor',direction='in',
                   length=3,width=1.0,color='k',pad=6,
                   labelsize=12,labelcolor='k')

    ax.grid(True, which='major', axis='both', alpha=0.4, c='#38b000')
    ax.grid(True, which='minor', axis='both', alpha=0.1, c='#38b000')
    
    ax.legend(loc='upper right')
    
    pdf_folder, png_folder = op_folders

    plt.savefig(os.path.join(pdf_folder, data_file)[:-3]+'pdf', bbox_inches='tight')
    plt.savefig(os.path.join(png_folder, data_file)[:-3]+'png', bbox_inches='tight')

def plot_counts(data, data_file, source_name, op_folders, x_ticks=(0.1, 0.01), energy_lo=0.2, energy_hi=1.0):
    energy = data[:,0]
    ebins  = data[:,1]
    rate   = data[:,2]
    rerr   = data[:,3]

    fig = plt.figure(figsize=(6,4), dpi=100)
    ax = fig.add_axes((0.1,0.1,0.9,0.9))

    ax.errorbar(energy, rate,
                xerr=ebins, yerr=rerr,
                fmt='+', elinewidth=0.8, alpha=0.8,
                c='#3f37c9', label='Counts')
    ax.set_yscale('log')
    ax.set_xlabel(r'Energy (keV)', fontsize=14)
    ax.set_ylabel(r'counts s$^{-1}$ keV$^{-1}$', fontsize=14)
    ax.set_title(f'{source_name} count rates', fontsize=16)
    ax.set_xlim(energy_lo, energy_hi)

    x_majticks, x_minticks = x_ticks
    ax.xaxis.set_major_locator(MultipleLocator(x_majticks))
    ax.xaxis.set_minor_locator(MultipleLocator(x_minticks))
    ax.tick_params(axis='x',which='major',direction='in',
                   length=6,width=1.5,color='k',pad=6,
                   labelsize=12,labelcolor='k')
    ax.tick_params(axis='x',which='minor',direction='in',
                   length=3,width=1.0,color='k',pad=6,
                   labelsize=12,labelcolor='k')

    ax.yaxis.set_major_locator(LogLocator(base=10))
    ax.yaxis.set_minor_locator(LogLocator(base=10,subs=(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9),numticks=12))
    ax.yaxis.set_major_formatter(FuncFormatter(log_formatter))
    ax.tick_params(axis='y',which='major',direction='in',
                   length=6,width=1.5,color='k',pad=6,
                   labelsize=12,labelcolor='k')
    ax.tick_params(axis='y',which='minor',direction='in',
                   length=3,width=1.0,color='k',pad=6,
                   labelsize=12,labelcolor='k')

    ax.grid(True, which='major', axis='both', alpha=0.4, c='#38b000')
    ax.grid(True, which='minor', axis='both', alpha=0.1, c='#38b000')

    #ax.legend(loc='upper right')

    pdf_folder, png_folder = op_folders

    plt.savefig(os.path.join(pdf_folder, data_file)[:-3]+'pdf', bbox_inches='tight')
    plt.savefig(os.path.join(png_folder, data_file)[:-3]+'png', bbox_inches='tight')
    
def plot_eufspec(data, data_file, op_folders, wave_lo=12.0, wave_hi=62.0):
    wavelength = data[:,0]
    wbins      = data[:,1]
    rate       = data[:,2]
    rerr       = data[:,3]
    eufspec    = data[:,4]
    
    fig = plt.figure(figsize=(6,4), dpi=100)
    ax = fig.add_axes((0.1,0.1,0.9,0.9))

    ax.errorbar(wavelength, rate, xerr=wbins, yerr=rerr, fmt='+', c='#3f37c9')
    ax.step(wavelength, eufspec, c='#ef233c', where='mid', zorder=3, label='Unfolded spectrum')
    ax.set_yscale('log')
    ax.set_xlabel(r'Wavelength $\lambda$ ($\AA$)', fontsize=14)
    ax.set_ylabel(r'Flux density $F_\lambda$ (erg s$^{-1}$ cm$^{-2}$ $\AA^{-1}$)', fontsize=14)
    ax.set_xlim(wave_lo, wave_hi)

    ax.xaxis.set_major_locator(MultipleLocator(2.0))
    ax.xaxis.set_minor_locator(MultipleLocator(1.0))
    ax.tick_params(axis='x',which='major',direction='in',
                   length=6,width=1.5,color='k',pad=6,
                   labelsize=12,labelcolor='k')
    ax.tick_params(axis='x',which='minor',direction='in',
                   length=3,width=1.0,color='k',pad=6,
                   labelsize=12,labelcolor='k')

    ax.yaxis.set_major_locator(LogLocator(base=10))
    ax.yaxis.set_minor_locator(LogLocator(base=10,subs=(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9),numticks=12))
    ax.yaxis.set_major_formatter(FuncFormatter(log_formatter))
    ax.tick_params(axis='y',which='major',direction='in',
                   length=6,width=1.5,color='k',pad=6,
                   labelsize=12,labelcolor='k')
    ax.tick_params(axis='y',which='minor',direction='in',
                   length=3,width=1.0,color='k',pad=6,
                   labelsize=12,labelcolor='k')

    ax.grid(True, which='major', axis='both', alpha=0.4, c='#38b000')
    ax.grid(True, which='minor', axis='both', alpha=0.1, c='#38b000')
    
    ax.legend(loc='upper right')
    
    pdf_folder, png_folder = op_folders
    
    plt.savefig(os.path.join(pdf_folder, data_file)[:-3]+'pdf', bbox_inches='tight')
    plt.savefig(os.path.join(png_folder, data_file)[:-3]+'png', bbox_inches='tight')
    
def plot_eufspec_keV(data, data_file, op_folders, energy_lo=0.2, energy_hi=1.0):
    energy  = data[:,0]
    ebins   = data[:,1]
    rate    = data[:,2]
    rerr    = data[:,3]
    eufspec = data[:,4]
    
    fig = plt.figure(figsize=(6,4), dpi=100)
    ax = fig.add_axes((0.1,0.1,0.9,0.9))

    ax.errorbar(energy, rate, xerr=ebins, yerr=rerr, fmt='+', c='#3f37c9')
    ax.step(energy, eufspec, c='#ef233c', where='mid', zorder=3, label='Unfolded spectrum')
    ax.set_yscale('log')
    ax.set_xlabel(r'Energy (keV)', fontsize=14)
    ax.set_ylabel(r'Flux density (Photons s$^{-1}$ cm$^{-2}$ keV$^{-1}$)', fontsize=14)
    ax.set_xlim(energy_lo, energy_hi)

    ax.xaxis.set_major_locator(MultipleLocator(0.2))
    ax.xaxis.set_minor_locator(MultipleLocator(0.02))
    ax.tick_params(axis='x',which='major',direction='in',
                   length=6,width=1.5,color='k',pad=6,
                   labelsize=12,labelcolor='k')
    ax.tick_params(axis='x',which='minor',direction='in',
                   length=3,width=1.0,color='k',pad=6,
                   labelsize=12,labelcolor='k')

    ax.yaxis.set_major_locator(LogLocator(base=10))
    #ax.yaxis.set_minor_locator(LogLocator(base=10,subs=(0.2,0.4,0.6,0.8),numticks=12))
    ax.yaxis.set_minor_locator(LogLocator(base=10,subs=(0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9),numticks=12))
    ax.yaxis.set_major_formatter(FuncFormatter(log_formatter))
    ax.tick_params(axis='y',which='major',direction='in',
                   length=6,width=1.5,color='k',pad=6,
                   labelsize=12,labelcolor='k')
    ax.tick_params(axis='y',which='minor',direction='in',
                   length=3,width=1.0,color='k',pad=6,
                   labelsize=12,labelcolor='k')

    ax.grid(True, which='major', axis='both', alpha=0.4, c='#38b000')
    ax.grid(True, which='minor', axis='both', alpha=0.1, c='#38b000')
    
    ax.legend(loc='lower right')
    
    pdf_folder, png_folder = op_folders
    
    plt.savefig(os.path.join(pdf_folder, data_file)[:-3]+'pdf', bbox_inches='tight')
    plt.savefig(os.path.join(png_folder, data_file)[:-3]+'png', bbox_inches='tight')

def plot_resid(data, data_file, op_folders, energy_lo=0.2, energy_hi=1.0, major_tick=1.0, minor_tick=0.5):
    energy  = data[:,0]
    resid   = data[:,2]
    
    fig, ax = plt.subplots(figsize=(6,4), dpi=100)

    plt.axhline(0, c='k', alpha=0.8, lw=1.2)
    plt.step(energy, resid)

    resid_lim = max([abs(min(resid)), abs(max(resid))])
    ax.set_ylim(-(round(resid_lim, 1)+0.2), (round(resid_lim, 1)+0.2))
    ax.set_xlabel(r'Energy (keV)', fontsize=14)
    ax.set_ylabel('Residual', fontsize=14)
    ax.set_xlim(energy_lo, energy_hi)
    
    resid_lim = max([abs(min(resid)), abs(max(resid))]); limfactor = 1.2
    ax.set_ylim(-(round(resid_lim, 1)*limfactor), (round(resid_lim, 1)*limfactor))
    #ax.set_ylim(-4, 4)

    ax.xaxis.set_major_locator(MultipleLocator(0.1))
    ax.xaxis.set_minor_locator(MultipleLocator(0.01))
    ax.tick_params(axis='x',which='major',direction='in',
                   length=6,width=1.5,color='k',pad=6,
                   labelsize=12,labelcolor='k')
    ax.tick_params(axis='x',which='minor',direction='in',
                   length=3,width=1.0,color='k',pad=6,
                   labelsize=12,labelcolor='k')

    ax.yaxis.set_major_locator(MultipleLocator(major_tick))
    ax.yaxis.set_minor_locator(MultipleLocator(minor_tick))
    ax.tick_params(axis='y',which='major',direction='in',
                   length=6,width=1.5,color='k',pad=6,
                   labelsize=12,labelcolor='k')
    ax.tick_params(axis='y',which='minor',direction='in',
                   length=3,width=1.0,color='k',pad=6,
                   labelsize=12,labelcolor='k')

    ax.grid(True, which='major', axis='both', alpha=0.4, c='#38b000', lw=0.8)
    ax.grid(True, which='minor', axis='both', alpha=0.1, c='#38b000', lw=0.8)
    
    pdf_folder, png_folder = op_folders

    plt.savefig(os.path.join(pdf_folder, data_file)[:-3]+'pdf', bbox_inches='tight')
    plt.savefig(os.path.join(png_folder, data_file)[:-3]+'png', bbox_inches='tight')

def group_plots_labels(data_files, obs_dates):
    plot_labels = []
    group_plot = {}
    for file in data_files:
        instrument = os.path.basename(file).split('-')[3].split('_')[0].upper()
        if instrument == 'ACIS':
            satellite = 'Chandra'
        elif instrument == 'PN':
            satellite = 'XMM'
        elif instrument == 'SIS1':
            satellite = 'ASCA'
        elif instrument == 'XTI':
            satellite = 'NICER'
        obs_id = os.path.basename(file).split('-')[2]
        obs_date = (obs_dates[f'{instrument}-{obs_id}'])

        if instrument == 'PN':
            plot_label = f'{obs_date} | {satellite}:EPIC-{instrument.lower()}'
            plot_labels.append(f'{obs_date} | {satellite}:EPIC-{instrument.lower()}')
        else:
            plot_label = f'{obs_date} | {satellite}:{instrument}'
            plot_labels.append(f'{obs_date} | {satellite}:{instrument}')
        plot_labels.append(plot_label)

        group_plot[f'{instrument}-{obs_id}'] = (file, plot_label)
    return group_plot
    
def overlay_edges(ax, url, energy_lims, elements, obs_edges, epsilon=0.02):
  df = pd.read_csv(url)
  energy_lo, energy_hi = energy_lims
  abs_edge = df.columns.tolist()[3:]
  for idx in df.index:
    element = df.loc[idx,'element']
    if element in elements:
      for ae in abs_edge:
        edge_value = df.loc[idx, ae]
        if edge_value >= energy_lo and edge_value <= energy_hi:
          for oe in obs_edges:
            if edge_value >= oe-epsilon and edge_value <= oe+epsilon:
              ax.axvline(edge_value, c='k', ls='--', lw=2)
              label_string = f'{element} {ae[:-5]} {edge_value:.3f} keV'
              ax.text(edge_value, 0.78, label_string, c='k', ha='right', va='top', rotation=90,
                      transform=ax.get_xaxis_transform())
                      
def get_edgedf(df):
  edgedf_keV = df.copy()  # DF containing edge data in keV
  edgedf_ang = pd.DataFrame() # Create an empty DF for storing edge data in angstroms
  collist = df.columns.tolist() # Store the DF column names in a list
  for i in range(len(df)): # Run a loop over all rows
    row = {}               # Create an empty dictionary that will store values for current row
    for col in collist:    # Run a loop over all columns
      if col in collist[3:]:  # Only for those columns which contain edge values...
        edge_ang = keV_to_ang(df.loc[i, col], sigfig=2) # Convert the value from keV to angstrom
        row[col] = edge_ang   # Store the angstrom value as a dictionary entry
      else:                        # For those columns which do not contain edge values...
        row[col] = df.loc[i, col]  # Store the DF value as is
    edgedf_ang = pd.concat([edgedf_ang, pd.DataFrame([row])], ignore_index=True)  # Append a row into the DF as a new row
  return edgedf_keV, edgedf_ang

def identify_edges_keV(edgedf_keV, energy_lims, elements, obs_edges_keV, epsilon=0.02):
  edge_keV = pd.DataFrame(columns=['element', 'edge', 'energy'])
  for i in edgedf_keV.index:
    element = edgedf_keV.loc[i, 'element']
    if element in elements:
      abs_edge = edgedf_keV.columns.tolist()[3:]
      for ae in abs_edge:
        edge_val = edgedf_keV.loc[i, ae]
        if edge_val >= energy_lims[0] and edge_val <= energy_lims[1]:
          for oe in obs_edges_keV:
            if edge_val >= oe-epsilon and edge_val <= oe+epsilon:
              edge_keV.loc[len(edge_keV.index)] = [element, ae, edge_val]
  return edge_keV
  
def identify_edges(edgedf_keV, energy_lims, elements, obs_edges_keV, epsilon=0.02):
  edge_df = pd.DataFrame(columns=['element', 'edge', 'energy', 'wavelength'])
  for i in edgedf_keV.index:
    element = edgedf_keV.loc[i, 'element']
    if element in elements:
      abs_edge = edgedf_keV.columns.tolist()[3:]
      for ae in abs_edge:
        edge_keV = edgedf_keV.loc[i, ae]
        if edge_keV >= energy_lims[0] and edge_keV <= energy_lims[1]:
          for oe in obs_edges_keV:
            if edge_keV >= oe-epsilon and edge_keV <= oe+epsilon:
              edge_df.loc[len(edge_df.index)] = [element, ae, edge_keV, keV_to_ang(edge_keV)]
  return edge_df
  
def plot_edge_overlay(source_name, idx, elem_list, wave_lims, ax, group_plot, sort_order, edge_df, flux_lo=1E-22, flux_hi=1E-11, text_yposn=0.78):
  wave_lo, wave_hi = wave_lims
  data = np.loadtxt(group_plot[sort_order[idx]][0], skiprows=3)
  wavelength = data[:,0]
  eufspec    = data[:,4]
  #ax.plot(wavelength, eufspec)
  ax.step(wavelength, eufspec, where='mid')

  if isinstance(elem_list, list):
    edge_df = edge_df[edge_df['element'].isin(elem_list)]

  for i in edge_df.index:
    wavelength_edge = edge_df.loc[i, 'wavelength']
    #label_string = edge_df.loc[i, 'element'] + ' ' + edge_df.loc[i, 'edge'][:-5]
    label_string = edge_df.loc[i, 'element'] + ' ' + edge_df.loc[i, 'edge'].replace('_', ' ')
    #ax.axvline(wavelength_edge, c='k', ls='--', lw=2, label='Literature')
    #.axvline(wavelength_edge, c='k', ls='--', lw=2, label=f'{label_string}')
    #ax.text(wavelength_edge, text_yposn, label_string, c='k', ha='right', va='top', rotation=90,
    #        transform=ax.get_xaxis_transform()
    if len(elem_list)>1:
        ax.axvline(wavelength_edge, c='k', ls='--', lw=2)
        ax.text(wavelength_edge, text_yposn, label_string, c='k', ha='right', va='top', rotation=90,
                transform=ax.get_xaxis_transform())
    else:
        ed_val = edge_df.loc[i,'wavelength']
        ax.axvline(wavelength_edge, c='k', ls='--', lw=2, label=f'{label_string}')
        ax.text(wavelength_edge, text_yposn, f'{ed_val:.2f} '+r'$\AA$', c='k', ha='right', va='top', rotation=90,
                transform=ax.get_xaxis_transform())
  
  ax.set_yscale('log')
  ax.set_xlabel(r'Wavelength $\lambda$ ($\AA$)', fontsize=14)
  ax.set_ylabel(r'Flux density $F_\lambda$ (erg s$^{-1}$ cm$^{-2}$ $\AA^{-1}$)', fontsize=14)
  ax.set_title(group_plot[sort_order[idx]][1])
  ax.set_xlim(wave_lo, wave_hi)
  ax.set_ylim(flux_lo, flux_hi)

  ax.xaxis.set_major_locator(MultipleLocator(2.0))
  ax.xaxis.set_minor_locator(MultipleLocator(1.0))
  ax.tick_params(axis='x',which='major',direction='in',
                length=6,width=1.5,color='k',pad=6,
                labelsize=12,labelcolor='k')
  ax.tick_params(axis='x',which='minor',direction='in',
                length=3,width=1.0,color='k',pad=6,
                labelsize=12,labelcolor='k')

  ax.yaxis.set_major_locator(LogLocator(base=10))
  ax.yaxis.set_minor_locator(LogLocator(base=10,subs=(0.2,0.4,0.6,0.8),numticks=12))
  ax.yaxis.set_major_formatter(FuncFormatter(log_formatter))
  ax.tick_params(axis='y',which='major',direction='in',
                length=6,width=1.5,color='k',pad=6,
                labelsize=12,labelcolor='k')
  ax.tick_params(axis='y',which='minor',direction='in',
                length=3,width=1.0,color='k',pad=6,
                labelsize=12,labelcolor='k')

  ax.grid(True, which='major', axis='both', alpha=0.4, c='#38b000')
  ax.grid(True, which='minor', axis='both', alpha=0.1, c='#38b000')

  instr = group_plot[sort_order[idx]][1].split('|')[1][1:].replace(':', '-')

  if isinstance(elem_list, str):
    op_filename = f'{source_name}-{instr}-uf-all-edges'
  else:
    op_filename = f'{source_name}-{instr}-uf-'
    for e in elem_list:
      op_filename += e + '-'
    op_filename += 'edges'
  return op_filename