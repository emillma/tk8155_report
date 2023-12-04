from dataclasses import dataclass
from typing import ClassVar
from matplotlib import pyplot as plt
import numpy as np
from functools import cached_property

@dataclass
class Splat:
    center: tuple[float, float]
    major_axis: tuple[float, float]
    shape: float
    
    _t = np.linspace(0, 2*np.pi, 200)
    _circle = np.array([np.cos(_t), np.sin(_t)])
    
    def __post_init__(self):
        v0 = np.array(self.major_axis)
        v1 = self.shape*np.array((-v0[1], v0[0]))
        self.T = np.array([v0, v1]).T
        
    
    
    @cached_property
    def ellipse_points(self):
        return self.T@self._circle + np.array(self.center)[:,None]
    
    def ellipse_points_transformed(self, T):
        return T@self.T@self._circle + np.array(self.center)[:,None]
        
    def plot_ellipse(self, ax):
        ax.plot(*self.ellipse_points)
            
    def __hash__(self) -> int:
        return hash((self.cx, self.cy, self.sx, self.sy, self.deg))
    
