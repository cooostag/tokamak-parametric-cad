#TODO: build here the Assembly
#TODO2: Parametrize and write a function for cylindrical section creation in another file and import the function here to create ports



#Basic libraries
from build123d import *
from ocp_vscode import show
import numpy as np


#Import of functions from other .py
from params import *
from Miller import miller_points
from vacum_chamber_param import vacum_chamber
from ToroidalF_Magnet_coil import toroidal_coil

n_points = 64
thickness_in = 8
thickness_out=4
gap_ : float = 5.0 #this will be later quantity to optimize
params_ = TokamakParams(epsilon=0.4) #potentially I can declare a type TokamaksParams function with different epsilon =...


Vacum_Chamber = vacum_chamber(n_points, params_, thickness_in, thickness_out)
TF_coil = toroidal_coil(params_,gap_, thickness_in, thickness_out)

Assembly = Vacum_Chamber.part + TF_coil.part

show(Vacum_Chamber, TF_coil, colors=["lightblue", "gold"], alphas=[1.0, 0.6])

print ("success")
