import xarray
import numpy as np
from matplotlib import pyplot as plt
from map_plots import quiver_plot

def climatology_figures(name, path_to_open, path_to_save, dx):
    dat = xarray.open_dataset(path_to_open)
    u = dat['uwnd'].sel(time = slice('1988-01-01', '2015-12-31')).groupby('time.month').mean(dim = 'time').squeeze()
    v = dat['vwnd'].sel(time = slice('1988-01-01', '2015-12-31')).groupby('time.month').mean(dim = 'time').squeeze()

    u_def = u.sel(month = [12, 1, 2]).mean(dim = 'month')
    v_def = v.sel(month = [12, 1, 2]).mean(dim = 'month')
    s_def = np.sqrt(u_def**2 + v_def**2)
    u_jja = u.sel(month = [6, 7, 8]).mean(dim = 'month')
    v_jja = v.sel(month = [6, 7, 8]).mean(dim = 'month')
    s_jja = np.sqrt(u_jja**2 + v_jja**2)

    fig, ax = quiver_plot(name, s_def, u.lat, v.lon, u_def/s_def, v_def/s_def, dx, 'gist_ncar', 0, 10, 0, -70, -80, 30, 'm/s')
    plt.savefig(path_to_save + name + '_def.png', bbox_inches = 'tight')
    fig, ax = quiver_plot(name, s_jja, u.lat, v.lon, u_jja/s_jja, v_jja/s_jja, dx, 'gist_ncar', 0, 10, 0, -70, -80, 30, 'm/s')
    plt.savefig(path_to_save + name + '_jja.png', bbox_inches = 'tight')

climatology_figures('CFSR', '/home/bock/Documents/tesis/datos/cfsr_atlsur_1979_2015.nc', '/home/bock/Documents/paper_vientos/figuras/', 4)
climatology_figures('NCEP R2', '/home/bock/Documents/tesis/datos/ncep2_atlsur_1979_2015.nc', '/home/bock/Documents/paper_vientos/figuras/', 1)
climatology_figures('NCEP R1', '/media/bock/Elements/tesis/tesis_vieja/ncep_v1/NCEP1_wind_daily_1948-2015.nc', '/home/bock/Documents/paper_vientos/figuras/', 1)
climatology_figures('ERA - Int', '/media/bock/Elements/tesis/tesis_vieja/era_int/kk.nc', '/home/bock/Documents/paper_vientos/figuras/', 4)
climatology_figures('CCMP', '/media/bock/Elements/tesis/tesis_vieja/ccmp/kk.nc', '/home/bock/Documents/paper_vientos/figuras/', 4)
