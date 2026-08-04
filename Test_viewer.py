from build123d import *
from ocp_vscode import show

# Create a sphere with a hole cut through it
with BuildPart() as sphere_with_hole:
    Sphere(radius=10)
    Cylinder(radius=4, height=30, mode=Mode.SUBTRACT)

# Render it live in your browser tab
show(sphere_with_hole)