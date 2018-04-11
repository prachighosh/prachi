import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-12, 13, 1000)

y = x**3 + 3*x + 3  

fig, ax = plt.subplots()
ax.plot(x, y)