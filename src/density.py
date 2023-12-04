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

v0 = np.array([0, 0])
v1 = np.array([0.5, sin60*.1])
# v1 = np.array([0,1])
v2 = np.array([1, 0])

x, y = np.einsum("ijk,ic->cjk", np.array([u, v, w]), np.array([v0, v1, v2]))

ca = np.array([1, 0, 0])
cb = np.array([1, 0, 0])
cc = np.array([0,0,1])

color = np.einsum("ijk,ic->jkc", np.array([u, v, w]), np.array([ca, cb, cc]))


# scale = lambda x: 0.1 + x * 0.9
alpha = (u*v*w)
k = 0.1
alpha = k *alpha + (1-k) * alpha**2
alpha[np.where((u < -1e-6) | (v < -1e-6) | (w < -1e-6))] = 0
alpha = alpha / alpha.max()

# alpha -= 0.1
color = color * alpha[:, :, None] + (1 - alpha[:, :, None]) * np.array([1, 1, 1])
color = np.clip(color, 0, 1)
# alpha[np.where(u + v > 1)] = 0

fig, ax = plt.subplots(1, 1, figsize=(8, 8))
ax: Axes
# mpl.rcParams["patch.force_edgecolor"] = False
ax.pcolormesh(x, y, color, shading="gouraud")
ax.set_xlim(0, 1)
ax.set_aspect("equal")


plt.show()
