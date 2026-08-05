from build123d import *
from ocp_vscode import show
import numpy as np
from sympy.abc import epsilon

# Modeling the surface following  Miller et al.
# Modeling the surface following  Miller et al.
n_points = 64  # resolution of the sampled curve
theta = np.linspace(0, 2 * np.pi, n_points, endpoint=False)  # closed curve, don't repeat the seam point

#Miller assumes cappa, delta, vau and epsilon are specified
# Reproducing the circle from the miller paper
# https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/simple-general-realistic-robust-analytic-tokamak-equilibria-part-1-limiter-and-divertor-tokamaks/0995989BC8BFB530B273A0666D0C0423

#testing the cirlce

epsilon=0.33
kappa=1
delta=0
vau=1
alfa=50
R0=alfa/epsilon
delta_hat = np.arcsin(delta)
R_s = R0 + alfa * np.cos(theta + delta_hat * np.sin(theta))
Z_s = alfa * kappa * np.sin(theta)

thickness = 4

points = list(zip(R_s.tolist(), Z_s.tolist()))



#Cannot use offset to create a hollow circle because build123d is not able to offset a closed geometry
#for this reason instead of using offset I will subtract 2 different profiles. This will be useful to
#model a not constant thicknes

with BuildSketch() as test_profile:
    with BuildLine():
        Spline(*points, periodic=True)
    make_face()

show(test_profile.sketch)

print ("Test")

#check cirlce geometry
#residual = np.sqrt((R_s - R0)**2 + Z_s**2) - a
#residual.max(), residual.min()

