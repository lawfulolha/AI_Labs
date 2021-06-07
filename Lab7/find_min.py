from genetic import Genetic
from pylab import *


f = lambda x, y: 3*x + 2*x**2 - 7*x**(1/2)
gen = Genetic(f, minim = 0, maxim = 15)
minim = gen.run()
print('Minimum found x =', minim[0], ', f(x) =', 3*minim[0] + 2*minim[0]**2 - 7*minim[0]**(1/2))