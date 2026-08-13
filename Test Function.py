#Test function
from build123d import *
from ocp_vscode import show


def create_cylinder (raggio, altezza):
    with BuildPart() as cylinder:
        Cylinder(radius=raggio, height=altezza)

    return cylinder

raggioX = 20
altezzaX = 30

CylinderX = create_cylinder (raggioX, altezzaX)

show(CylinderX)

print ("Test")