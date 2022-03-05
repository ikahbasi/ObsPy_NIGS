import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

# frequency response
f = range(101)
a = np.random.random(len(f))
# interpolate for better plot
func = interp1d(f, a)
f = np.linspace(0, 100, num=10000, endpoint=True)
a = func(f)
# water level
w = [0.4]*len(f)

# plot frequency response
plt.plot(f, a, 'k')
# plot water level
plt.fill_between(f, a, w, where=a<=w, color='b', alpha=.3)
#
plt.ylabel('Amplitude')
plt.xlabel('Frequency')
plt.show()
