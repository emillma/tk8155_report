from pathlib import Path
import numpy as np
from matplotlib import pyplot as plt


this_dir = Path(__file__).parent
file = this_dir / "count.npy"
arr: np.ndarray = np.load(file)

print(arr.shape)
plt.plot(*arr.T)
plt.ylabel("Splat Count")
plt.xlabel("Iteration")
plt.show()
