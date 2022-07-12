from fenics import *
from parameters import my_model

my_model.initialise()

T = my_model.T.T
XDMFFile("Results/T.xdmf").write(T)
