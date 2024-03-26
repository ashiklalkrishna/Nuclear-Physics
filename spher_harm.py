import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import sph_harm
plt.rcParams['text.usetex'] = False

theta=np.linspace(0, np.pi, 100)
phi=np.linspace(0, 2*np.pi, 100)
theta, phi=np.meshgrid(theta, phi)

def plot_Y(ax, el, m):
    Y=sph_harm(abs(m), el, phi, theta)

    if m<0:
        Y=np.sqrt(2)*(-1)**m*Y.imag
    elif m>0:
        Y=np.sqrt(2)*(-1)**m*Y.real
        
    Yx=np.abs(Y)*np.sin(theta)*np.sin(phi)
    Yy=np.abs(Y)*np.sin(theta)*np.cos(phi)
    Yz=np.abs(Y)*np.cos(theta)

    cmap = plt.cm.ScalarMappable(cmap=plt.get_cmap('cool'))
    cmap.set_clim(-0.5, 0.5)

    ax.plot_surface(Yx, Yy, Yz, facecolors=cmap.to_rgba(Y.real), 
                    rstride=2, cstride=2)
    
    ax.set_title(r'$Y_{{{},{}}}$'.format(el, m))
    ax_lim=0.35
    ax.set_xlim(-ax_lim, ax_lim)
    ax.set_ylim(-ax_lim, ax_lim)
    ax.set_zlim(-ax_lim, ax_lim)
    ax.axis('off')

el_max=3
fig=plt.figure(dpi=100)
spec=gridspec.GridSpec(ncols=2*el_max+1, nrows=el_max+1, figure=fig)
for el in range(el_max+1):
    for m_el in range(-el, el+1):
        ax = fig.add_subplot(spec[el, m_el+el_max], projection='3d')
        plot_Y(ax, el, m_el)
        
plt.tight_layout()
plt.show()
