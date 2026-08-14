#This file is to create Miller profiles before part creation as Vacum Chamber and toroidal magnetic field coil need it

import numpy as np

from params import TokamakParams
from ocp_vscode import show

def miller_points (n_points, params_: TokamakParams, thickness_outboard: float =0, thickness_inboard: float =0):
    theta = np.linspace(0, 2 * np.pi, n_points, endpoint=False)

    if thickness_outboard != thickness_inboard:
        # simple smooth blend based on cos(theta): +1 at outboard (theta=0), -1 at inboard (theta=pi)
        thickness_theta = (thickness_outboard + thickness_inboard) / 2 \
                          + (thickness_outboard - thickness_inboard) / 2 * np.cos(theta)
        # plot the function in different file to understand / remember good what the funciton does

        alfa_theta = params_.alfa - thickness_theta

    else:
        alfa_theta = params_.alfa

    alfa_min = np.min(alfa_theta)
    alfa_max = np.max(alfa_theta)
    assert alfa_min > 0, (
        f"Non-physical geometry: minimum effective minor radius is {alfa_min:.3f} "
        f"(alfa={params_.alfa}); thickness too large somewhere, curve would self-intersect."
    )
    assert alfa_max <= params_.alfa, (
        f"Non-physical geometry: effective minor radius {alfa_max:.3f} exceeds "
        f"nominal alfa={params_.alfa}; thickness is negative somewhere."
    )

    delta_hat = np.arcsin(params_.delta)
    R_s = params_.R0 + alfa_theta * np.cos(theta + delta_hat * np.sin(theta))
    Z_s = alfa_theta * params_.kappa * np.sin(theta)
    points = list(zip(R_s.tolist(), Z_s.tolist()))

    return points


Tparams = TokamakParams ()
npoints = 64
#thick_i = 4
#thick_o = 4

Miller_test = miller_points (npoints, Tparams )


print (Miller_test)

