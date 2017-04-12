from pylab import *

figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

labels = 'Spring', 'Summer', 'Autumn', 'Winter'

x = [15, 30, 45, 10]

explode=(0.1, 0.1, 0.1, 0.1)

pie(x, explode=explode, labels=labels,
autopct='%1.1f%%', startangle=67)

title('Rainy days by season')

show()
