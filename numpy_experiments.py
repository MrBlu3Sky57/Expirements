from matplotlib import pyplot as pp
import numpy as np
import math



values = np.array([[i * i] for i in range(-100, 101)])

pp.plot(values)
pp.show()
