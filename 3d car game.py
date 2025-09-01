
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

# -----------------------------
# Window & Camera State
# -----------------------------
window_width = 800
window_height = 600

camera_x = 0.0
camera_y = 3.0
camera_z = 10.0
look_x = 0.0
look_y = 0.0
look_z = 0.0

UP_X, UP_Y, UP_Z = 0.0, 1.0, 0.0


player_x = 0.0
player_y = 0.0
player_z = 0.0
player_yaw = 0.0
player_speed = 0.0

MAX_SPEED = 0.53
ACCEL, FRICTION = 0.00105, 0.00095
TURN_RATE = 0.21
WHEEL_X_OFFSET = 0.57

