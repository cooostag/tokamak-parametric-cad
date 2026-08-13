from build123d import *
from ocp_vscode import show
import numpy as np
from sympy.abc import epsilon

#When starting run python -m ocp_vscode to start the CAD viewer

# Modeling the surface following  Miller et al.
# Modeling the surface following  Miller et al.
n_points = 64  # resolution of the sampled curve
theta = np.linspace(0, 2 * np.pi, n_points, endpoint=False)  # closed curve, don't repeat the seam point

#Miller assumes cappa, delta, vau and epsilon are specified
# Reproducing the circle from the miller paper
# https://www.cambridge.org/core/journals/journal-of-plasma-physics/article/simple-general-realistic-robust-analytic-tokamak-equilibria-part-1-limiter-and-divertor-tokamaks/0995989BC8BFB530B273A0666D0C0423

#the triangularity values are e=0.4, kappa=2 delta=0.4 v=1
epsilon=0.4
kappa=1
delta=0.75
vau=1
alfa=50
R0=alfa/epsilon
delta_hat = np.arcsin(delta)
R_s = R0 + alfa * np.cos(theta + delta_hat * np.sin(theta))
Z_s = alfa * kappa * np.sin(theta)

thickness = 4 # thickness of the wall
R_internal = 150 # distance from revolution of the center of the vacuum's chamber profile

points_outer = list(zip(R_s.tolist(), Z_s.tolist()))
#list and zip to make a 1:1 matching (and organized in a list) between the 2 coordinates to identify the points and pass it as

# Inner boundary: same Miller curve, smaller minor radius (alfa - thickness)
alfa_inner = alfa - thickness
R_s_inner = R0 + alfa_inner * np.cos(theta + delta_hat * np.sin(theta))
Z_s_inner = alfa_inner * kappa * np.sin(theta)
points_inner = list(zip(R_s_inner.tolist(), Z_s_inner.tolist()))

#Cannot use offset to create a hollow circle because build123d is not able to offset a closed geometry
#for this reason instead of using offset I will subtract 2 different profiles. This will be useful to
#model a not constant thicknes

with BuildSketch() as vessel_profile:
    with BuildLine():
        Spline(*points_outer, periodic=True)
    outer_face= make_face()

with BuildSketch() as inner_sketch:
    with BuildLine():
        Spline(*points_inner, periodic=True)
    inner_face = make_face()

vessel_face = outer_face - inner_face  # or Face subtraction, check exact API

moved_vessel_face = vessel_face.moved(Location((R_internal, 0, 0)))

#show(moved_vessel_face)

print ("sub part 1")


with BuildPart() as VC_3D:
    # Revolve the 2D sketch face around that axis
    revolve(profiles=moved_vessel_face, axis=Axis.Y, revolution_arc=360)

# Show the full 3D vessel!
#show(VC_3D)

print ("Sub part 2")


#check cirlce geometry -> Check succesfulll
#residual = np.sqrt((R_s - R0)**2 + Z_s**2) - a
#residual.max(), residual.min()

#Next: Cut a cylinder
#1 create a cylinder with build part
#2 put it at the right place!
#3 subtract the cylinder from the vacum chamber

#1 create cylinder
#2 parametric

#test this
R_port= 10
height_port= 80

#Create cylinder and put it at the right place direcly
with BuildPart() as cylinder_base_port:
    with Locations((0,0,R_internal + 150)):
        Cylinder (radius=R_port, height=height_port)

show  (cylinder_base_port)

print ("Success")


poloidal_theta = 45 # is the angle to parametrize the rotation of the cylinder
cylinder_base_port = cylinder_base_port.part.rotate(Axis.Y, poloidal_theta)

show  (cylinder_base_port, VC_3D)

print ("Success")

#use locations with rotate and an angle parametrized to decide where to cut it, it needs though to be a poloidal rotation
# increase height of cylinder
#show (cylinder_base_port, VC_3D)
#Simple cut of parts like this is not possible
VC_withPort= VC_3D.part- cylinder_base_port

show  (VC_withPort)


print ("Success")