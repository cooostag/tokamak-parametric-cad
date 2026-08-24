from build123d import *
from ocp_vscode import show
import numpy as np
from params import *
from Miller import miller_points


def vacum_chamber (n_points, vessel_params: TokamakParams, vc_thickness_in:float, vc_thickness_out:float) :
    outer_points_ = miller_points(n_points, vessel_params)
    inner_points_ = miller_points(n_points, vessel_params, vc_thickness_in, vc_thickness_out)

    with BuildSketch() as vessel_profile:
        with BuildLine():
            Spline(*outer_points_, periodic=True)
        outer_face= make_face()

    with BuildSketch() as inner_sketch:
        with BuildLine():
            Spline(*inner_points_, periodic=True)
        inner_face = make_face()

    vessel_face = outer_face - inner_face  # or Face subtraction, check exact API
    moved_vessel_face = vessel_face.moved(Location((params_.R0, 0, 0)))

    with BuildPart() as vacum_chamber:
        revolve(moved_vessel_face, axis=Axis.Y, revolution_arc=360)

    return vacum_chamber

params_= TokamakParams()
n_points = 64
thickness_in = 8
thickness_out=4

Vacum_Chamber = vacum_chamber(n_points, params_, thickness_in, thickness_out)

show(Vacum_Chamber)

print ("success")





