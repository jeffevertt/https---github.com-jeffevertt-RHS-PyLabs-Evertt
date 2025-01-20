# 3d space - right handed, y up (z forward, x left)
from lib.window_physics3d import *
from lib.winobj_plane import Plane
from lib.winobj_cuboid import Cuboid
from lib.utils import *
from typing import List

def setupLevel(window):
    # ground plane
    Plane( window, v3(0, -10, 0), v3_up(), color = "green" )
    
    # cuboid
    Cuboid( window, v3(0, 0, 0), v3(10, 10, 10), color = "#8A2BE2" )

def updateLevel(window, deltaTime):
    pass

####################################################################################################
############################## DO NOT MODIFY  METHODS BELOW THIS LINE ##############################
########################## EXCEPT TO REMOVE TUTORIAL GAME CONFIG ARGUMENT  #########################
####################################################################################################
WindowPhysics3D("Lab 18: Cuboid Physics!", 
                cameraPos = v3(0,0,-30),
                setupLevelFn = setupLevel,
                updateLevelFn = updateLevel).runGameLoop()