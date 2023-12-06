from dataclasses import dataclass, field
import numpy as np
from functools import cached_property
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import matplotlib


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from splat import Splat

matplotlib.use("QtAgg")


@dataclass
class Projection:
    near: float
    height: float
    far: float
    
    fig_world: plt.Figure = field(init=False)
    ax_world: Axes = field(init=False)

    fig_proj: plt.Figure = field(init=False)
    ax_proj: Axes = field(init=False)

    def __post_init__(self):
        self.fig_world, self.ax_world = plt.subplots(1, 1)
        self.ax_world.set_aspect("equal")
        self.fig_proj, self.ax_proj = plt.subplots(1, 1,)
        self.ax_proj.set_aspect("equal")

        n, f, h = self.near, self.far, self.height
        hf = h * (f / n)
        for i in np.linspace(-1, 1, 11):
            x = np.linspace(n, f, 11)
            y = np.linspace(i * h, i * hf, 11)
            self.plot_world(
                x, y, c="k", alpha=0.5, marker=".", markersize=1, linewidth=0.5
            )
            self.plot_proj(
                x, y, c="k", alpha=0.5, marker=".", markersize=1, linewidth=0.5
            )
    
        
    def project(self, x, y):
        u = 2 * (x - self.near) / (self.far - self.near)
        v = (y * self.near) / (x * self.height)
        return np.array([u, v])

    @cached_property
    def square_points(self):
        n, f, h = self.near, self.far, self.height
        hf = h * (f / n)
        return np.array([[n, h], [f, hf], [f, -hf], [n, -h], [n, h]]).T

    def plot_world(self, x, y, **kwargs):
        self.ax_world.plot(x, y, **kwargs)

    def plot_proj(self, x, y, project=True, **kwargs):
        if project:
            x, y = self.project(x, y)
        self.ax_proj.plot(x, y, **kwargs)

    def jacobian(self, x, y):
        dudx = 2 / (self.far - self.near)
        dudy = 0
        dvdx = -(1 / x**2) * (y * self.near) / self.height
        dvdy = self.near / (x * self.height)
        return np.array([[dudx, dudy], [dvdx, dvdy]])

    def plot_approx_splat(self, s: "Splat", **kwargs):
        center = self.project(*s.center)
        x, y = self.jacobian(*s.center) @ s.T @ s._circle + center[:, None]
        self.ax_proj.plot(x, y, "--", **kwargs)
        self.ax_proj.plot(
            [center[0], center[0]], [np.amin(y), np.amax(y)], "--", **kwargs
        )

    def tight(self):
        self.fig_world.tight_layout()
        self.fig_proj.tight_layout()
