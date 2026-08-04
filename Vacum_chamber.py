#FIRST easy profile

from build123d import *
from ocp_vscode import show

#VC = Vacum Chamber

thickness = 5
delta_radius = 50
height= 50
bend_radius = 0.5
R_internal= 150

#Use location to move the D to a distance of inner radius
with BuildSketch() as VC_Profile:
    with Locations((R_internal, 0)):
        with BuildLine() as D_Profile:
             #Vertical inner straight wall
            line1 = Line((0,0), (0,height/2))

            #smoth arc of the D Shape

            line2 = Spline (
                (0, height/2),
                (delta_radius, 0),
                tangents = [(1,0),(0,-1)]
            )

            offset(amount= thickness, side=Side.RIGHT)
        make_face()
        mirror (about= Plane.XZ)
    #revolve(VC_Profile,Axis= Axis.Y,)

moved_face = VC_Profile.sketch.moved(Location((R_internal, 0, 0)))

with BuildPart() as VC_3D:
    # Revolve the 2D sketch face around that axis
    revolve(profiles=moved_face, axis=Axis.Y, revolution_arc=360)

# Show the full 3D vessel!
show(VC_3D)


#show ()


#GOAL:
# 1 - Model the vacum chaber and 1 coil (with clearance)
# 2- translate in JAX
# 3 - Mesh with gmesh