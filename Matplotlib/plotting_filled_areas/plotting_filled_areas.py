from matplotlib.pyplot import figure, show, gca
import numpy as np

x = np.arange(0.0, 2, 0.01)

y1 = np.sin(2*np.pi*x)
y2 = 1.2*np.sin(4*np.pi*x)

fig = figure()
ax = gca()

ax.plot(x, y1, x, y2, color='black')

ax.fill_between(x, y1, y2, where=y2>=y1,
               facecolor='darkblue', interpolate=True)
ax.fill_between(x, y1, y2, where=y2<=y1,
               facecolor='deeppink', interpolate=True)
ax.set_title('filled between')

show()
