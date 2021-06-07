import matplotlib.pyplot as plt
from pylab import *

x = linspace(0, 15, 100)
y = 3*x + 2*x**2 - 7*x**(1/2)

plot(x, y)

show()