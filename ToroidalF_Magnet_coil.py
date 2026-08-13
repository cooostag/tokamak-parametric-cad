#Toroidal field (TF) coil — a second torus-like shape that has to sit outside your vacuum vessel with a defined clearance gap

from params import *
from build123d import *
from ocp_vscode import show

#coild_width, coil_height all need to be put in params file or in a 2nd TF coil param
coil_width: float = 4.0
coil_height: float = 4.0

gap_ : float = 5.0
# R = 125 + 50 + 5 + 5 = 185

#calling the functions within the file, is it good practice?
params_ = TokamakParams()
coilR0 = coil_R0(params_)

print ("stoP")

def toroidal_coil (gap):
    coil_Re = coilR0 + params_.alfa + params_.thickness + gap

#Simplifcation: rectangular coil -> Improve to better geometry
    with BuildSketch() as coil_profile:
        with Locations((coil_Re, 0)):
            Rectangle(width=coil_width, height=coil_height)

    with BuildPart() as coil:
        revolve(profiles=coil_profile.sketch, axis=Axis.Y, revolution_arc=360)

    return coil


TF_coil = toroidal_coil(gap_)
show(TF_coil) # remove the show, was done only for check practice

print ("heyholetsgo")


#def build_tf_coil(vessel_params: TokamakParams, gap: float, coil_width: float, coil_height: float):
 #   R0 = coil_R0(vessel_params)
  #  coil_center_radius = R0 + coil_bore_radius(vessel_params, gap)