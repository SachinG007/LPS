
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

xr = 0.55		#position of the receiver
yr = 0.95
xt = 2.04		#position of teh transmitter
yt = 2.57
tan = 3			#value of the tan(theta) from saqibs part

func = lambda x : sqrt( (x - xr)**2 + (x*y - yr)**2 ) + sqrt( (x - xt)**2 + (x*y - yt)**2 );

x_guess = 4
x_value = fsolve(func,x_guess)
print "The solution is tau = %f" % x_value
