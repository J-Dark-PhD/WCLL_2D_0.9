from fenics import *
import matplotlib.pyplot as plt

from parameters import my_model

my_model.initialise()

# plt.figure()
# plot(my_model.T)
# plt.savefig("out.png")

T = my_model.T.T
XDMFFile("Results/T.xdmf").write(T)
