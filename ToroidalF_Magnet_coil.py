#Toroidal field (TF) coil —  Magnet that wraps around the vacum chamber in a poloidal plane. Can be repeated and placed at different angle

from params import *
from build123d import *
from ocp_vscode import show
from Miller import miller_points

#coild_width, coil_height all need to be put in params file or in a 2nd TF coil param
#coil_width_: float = 4.0
#coil_height_: float = 4.0
coil_thick_in: float = 8.0
coil_thick_out: float = 4.0
gap_ : float = 5.0
# R = 125 + 50 + 5 + 5 = 185

print ("stoP")

def toroidal_coil (vessel_params: TokamakParams, gap,conductor_radius:float, coil_thickness_in:float=0, coil_thickness_out:float=0):
    coilR0 = coil_R0(vessel_params)
    #coil_Re = coilR0 + vessel_params.alfa + vessel_params.thickness + gap

    outer_points = miller_points(64,vessel_params)
    #inner_points = miller_points(64,vessel_params,coil_thickness_out,coil_thickness_in)

    with BuildLine() as path:
        Spline(*outer_points, periodic=True)  #* unpacks the list and passes every point as separate as required by Spline

    with BuildPart() as single_tf_coil:
        with BuildSketch(Plane(origin=path.line @ 0, z_dir=path.line % 0)) as coil_cross_section:
            Circle(radius=conductor_radius)  # this is the coil's own "thickness" — independent, small
        sweep(path=path.line)

    return single_tf_coil

#Test the function
params_ = TokamakParams(epsilon=0.4) #potentially I can declare a type TokamaksParams function with different epsilon =...
conductor_r= 4.0
TF_coil = toroidal_coil(params_,gap_, coil_thick_in, coil_thick_out, conductor_r)
show(TF_coil) # remove the show, was done only for check practice

print ("heyholetsgo")