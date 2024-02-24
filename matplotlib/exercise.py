import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0.0, 5.0, 0.1)
y = np.cos(2 * np.pi * x) * np.exp(-x)


plt.plot(x,y,'black')
plt.xlabel('Abscissa',c='green')

plt.ylabel('Ordinate',c='green')
plt.title('Figure Title')
plt.text(1, 0.4, "θ = 60°")
plt.annotate("2nd crest", xy=(2, 0.16), xytext=(2.5, 0.3),arrowprops=dict(color='green'))
plt.scatter(x,y)
plt.grid()
plt.show()
