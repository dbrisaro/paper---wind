"""
El quiver plot grafica un campo en pcolormesh y arriba vectores.
"""

def quiver_plot(name, x, lat, lon, u, v, dx, cmap, vmi, vma, lat_i, lat_f, lon_i, lon_f, cbar_label):
    import cartopy.crs as ccrs
    from cartopy.feature import NaturalEarthFeature
    from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
    import matplotlib.gridspec as gridspec
    import shapely.geometry as sgeom
    from matplotlib import pyplot as plt
    import numpy as np
    import xarray

    x0, y0 = np.meshgrid(u.lon, v.lat)
    x1, y1 = np.meshgrid(lon, lat)

    fig = plt.figure(figsize = (10,12))
    ax = fig.add_subplot(111, projection = ccrs.Mercator())
    ax.set_extent([lon_i, lon_f, lat_f, lat_i], crs = ccrs.PlateCarree())
    ti = NaturalEarthFeature('physical', 'land', '50m', edgecolor='black', facecolor='white')
    ax.add_feature(ti)
    ax.coastlines(resolution = '50m')
    gl = ax.gridlines(crs = ccrs.PlateCarree(central_longitude = 0), draw_labels = True, color = 'white', linestyle = '--', linewidth = 0.4)
    gl.xlabels_top = gl.ylabels_right = False
    gl.xformatter = LONGITUDE_FORMATTER
    gl.yformatter = LATITUDE_FORMATTER
    cl = ax.pcolormesh(x1, y1, x, transform = ccrs.PlateCarree(), cmap = cmap, vmin = vmi, vmax = vma)
    qvr = ax.quiver(x0[::dx, ::dx], y0[::dx, ::dx], u.values[::dx, ::dx], v.values[::dx, ::dx], units = 'xy', scale = 0.2/111139, transform = ccrs.PlateCarree())
    cbar = fig.colorbar(cl, ax = ax, shrink = 0.7)
    cbar.ax.set_ylabel('m/s')
    ax.text(0.1, 0.9, name, transform = ax.transAxes, size = 15)

    return fig, ax
