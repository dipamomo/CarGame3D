
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

MAX_SPEED = 0.53
ACCEL, FRICTION = 0.00105, 0.00095
TURN_RATE = 0.21
WHEEL_X_OFFSET = 0.57

moving_forward, moving_brake = False, False
turning_left, turning_right = False, False

first_person_view = False
game_over = False
score = 0

LANE_WIDTH = 3.05
ROAD_WIDTH = LANE_WIDTH * 3.5

SEGMENT_LEN = 18.9
NUM_SEGMENTS = 11
TERRAIN_SIZE = 192.0

road_segments = []
trees, houses, house_colors = [], [], []

NUM_TREES = 58
NUM_HOUSES = 22

STRIPE_LEN = 2.6
GAP_LEN = 2.6
STRIPE_WIDTH = 0.30

HIT_X = 0.95
HIT_Z = 1.60

class NpcCar:
    def __init__(self, pos_x, pos_z, velocity, color_rgb):
        self.x, self.z = float(pos_x), float(pos_z)
        self.speed = float(velocity)
        self.color = (float(color_rgb[0]), float(color_rgb[1]), float(color_rgb[2]))
        self.passed = False

npcs = []
cpu_spawn_timer = 0
cpu_spawn_interval = 250

BASE_NPC_SPEED = 0.23
SPAWN_DISTANCE = 77
OVERTAKE_BONUS = 115

SHAKE_FRAMES = 35
SHAKE_MAG = 0.35
shake_frames = 0
shake_phase = 0.0

