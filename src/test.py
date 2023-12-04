from matplotlib import pyplot as plt
import numpy as np
from splat import Splat
from projection import Projection
from multiprocessing import shared_memory


p = Projection(1, 0.5, 16)
s1 = Splat((12.5, 0), (2, -2), 0.3)
s2 = Splat((13, 0), (2, 2), 0.3)

for s, c in zip([s1, s2], ["C0", "C1"]):
    p.plot_world(*s.ellipse_points, c=c)
    p.plot_proj(*s.ellipse_points, c=c)
    p.plot_approx_splat(s, c=c)

# p.plot_world(*p.square_points)
# p.plot_proj(p.square_points)

# fig, ax = plt.subplots(1,1)
# ax.set_aspect('equal')
# s1.plot_ellipse(ax)
# p.plot_square(ax)
# # ax.plot(*p.square_points)

# fig, ax = plt.subplots(1,1)
# ax.set_aspect('equal')

# ax = axs[1]
# ax.plot(*p.project(s1.ellipse_points))
# ax.plot(*p.project(p.square_points))

# p.tight()
plt.show()
