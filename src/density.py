from matplotlib import pyplot as plt
from matplotlib.axes import Axes
import matplotlib as mpl
import numpy as np
import sympy as sp


mpl.use("Qt5Agg")
u, v = sp.symbols("u v")
a = sp.Matrix([(u * v * (1 - u - v)) ** 2])
jac = a.jacobian([u, v])
print(a.jacobian([u, v]))

sin60 = np.sqrt(3) / 2

n = 101
grid = np.mgrid[0 : 1 : n * 1j, 0 : 1 : n * 1j]


u, v = grid
w = 1 - u - v

def alpha1(u, v, w):
    return (u*v*w)
    
def alpha2(u, v, w):
    return (u*v*w)**2

def alpha3(u, v, w):
    return (1-u)*(1-v)*np.minimum(2*w,1)
# def alpha3(u, v, w):
#     return (u*v*w)**2 *0.95 + (u*v*w) *0.05 

def final(e, k):
    def alpha3(u, v, w):
        A = np.array([[1,0,0],[1, 1, 1], [1, 2, 3]])
        x = np.array([e,1,0])
        a,b,c = np.linalg.solve(A, x)
        uvw = np.minimum(k*np.array([u,v,w]), 1)
        u,v,w = a*uvw + b*uvw**2 + c*uvw**3
        return u*v*w
    return alpha3

def dense(ax, vs, cs, alpha_func):
    x, y = np.einsum("ijk,ic->cjk", np.array([u, v, w]), vs)
    color = np.einsum("ijk,ic->jkc", np.array([u, v, w]), cs)

    alpha = alpha_func(u, v, w)
    alpha[np.where((u < -1e-6) | (v < -1e-6) | (w < -1e-6))] = 0
    alpha = (alpha-alpha.min()) / (alpha.max()-alpha.min())
    alpha[np.where((u < -1e-6) | (v < -1e-6) | (w < -1e-6))] = 0
    alpha = alpha[:,:,None] * color[:,:,3:]
    color = color[...,:3] * alpha + (1 - alpha) * np.array([1, 1, 1])
    color = np.clip(color, 0, 1)
    
    ax.pcolormesh(x, y, color, shading="gouraud")
    ax.plot(*np.vstack((vs, vs[0])).T, ":k", alpha=0.1)
    
fig, ax = plt.subplots(1, 1)
ax: Axes
v1 = np.array([[0,0],
              [1,0],
              [.5,sin60]])
c = np.array([[1,0,0,1],
              [1,0,0,1],
              [0,0,1,1]])

dense(ax, v1, c, alpha1)
dense(ax, v1 + np.array([[1,0]]), c, alpha2)
dense(ax, v1+ np.array([[2,0]]), c, alpha3)
dense(ax, v1+ np.array([[0,-1]]), c, final(.3,2))
dense(ax, v1+ np.array([[1,-1]]), c, final(.5,3))
dense(ax, v1+ np.array([[2,-1]]), c, final(2,4))
# mpl.rcParams["patch.force_edgecolor"] = False
ax.set_xlim(-.1, 3.1)
ax.set_ylim(-1.1, 1.1)
ax.set_aspect("equal")


plt.show()
