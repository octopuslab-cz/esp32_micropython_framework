# octopusLAB - basic lib. transform math

__version__ = "0.0.5"

"""
inspir: https://github.com/aquila12/me-arm-ik
todo
class: point2d / point3d
gimbal: 2 x pol / const r
IK: invers kinematics
for robotic arm (3/5 axes)
drawbot and polar graph math.
"""

import math


point0_2d = 0, 0
point0_3d = 0, 0, 0

RADIANS = 0
DEGREES = 1

arm = 70 #delta1
l1 = arm
l2 = arm


class Point2D():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, add):
        return Point2D(self.x + add.x, self.y + add.y)

    def __str__(self):
        return(self.x, self.y)


# point: p = Point2D(x,y)
def distance2D(p1, p2, rr = 5):  # default round rr
    # x1 = p1[0], y2 = p1[1]
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return round(math.sqrt(dx*dx + dy*dy), rr)


# point: p = x, y
def distance2(p1, p2, rr = 5):  # default round rr
    # x1 = p1[0], y2 = p1[1]
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    return round(math.sqrt(dx*dx + dy*dy), rr)


def move_2d_line(p_start, p_stop, steps = 300, max_dist = 100, debug = False): # default: one step per one unit
    unit = max_dist/steps
    move_dist = distance2(p_start, p_stop)
    move_steps = move_dist/unit
    if debug:
        print(unit, move_dist, move_steps)

    x = p_start[0]
    y = p_start[1]
    dx = p_stop[0] - x
    dy = p_stop[1] - y
    ddx = dx/move_steps
    ddy = dy/move_steps

    points = []
    for step in range(move_steps):
        if debug:
            print(step, x, y) # test / debug
        points.append((x, y))
        x += ddx
        y += ddy

    points.append((p_stop[0], p_stop[1]))
    return points


def polar2cart(r, alfa, rr = 3):
    x = r * math.cos(math.radians(alfa))
    y = r * math.sin(math.radians(alfa))
    return round(x, rr), round(y, rr)


def cart2polar(point):
    x = point[0]
    y = point[1]
    r = distance2((0, 0), point)
    c = x / r
    s = y / r

    #Safety!
    if(s > 1): s = 1
    if(c > 1): c = 1
    if(s < -1): s = -1
    if(c < -1): c = -1

    alfa = math.degrees(math.acos(c))
    if(s < 0): alfa *= -1

    return(r, alfa)


def cosangle(opp, adj1, adj2):
    # cosangle(1,1,1) => 60, True

    # Cosine rule:
    # C^2 = A^2 + B^2 - 2*A*B*cos(angle_AB)
    # cos(angle_AB) = (A^2 + B^2 - C^2)/(2*A*B)
    # C is opposite
    # A, B are adjacent

    alfa = 0
    direct = True

    den = 2*adj1*adj2
    if(den==0):
        direct = False
        return alfa, direct

    c = (adj1*adj1 + adj2*adj2 - opp*opp)/den

    if(c>1 or c<-1):
        direct = False
        return alfa, direct

    alfa = math.degrees(math.acos(c))

    return alfa, direct


# https://ashwinnarayan.blogspot.com/2014/07/inverse-kinematics-for-2dof-arm.html
#IK for just the 2 links
def invkin2(point2d):
    """Returns the angles of the first two links
    in the robotic arm as a list.
    returns -> (th1, th2)
    input:
    x - The x coordinate of the effector
    y - The y coordinate of the effector
    angleMode - tells the function to give the angle in
                degrees/radians. Default is degrees
    output:
    th1 - angle of the first link w.r.t ground
    th2 - angle of the second link w.r.t the first"""
    x, y = point2d.x, point2d.y

    #stuff for calculating th2
    r_2 = x * x+ y * y
    l_sq = l1 * l1 + l2 * l2
    term2 = (r_2 - l_sq)/(2*l1*l2)
    term1 = ((1 - term2**2)**0.5)*-1

    #calculate th2
    th2 = math.atan2(term1, term2)
    #optional line. Comment this one out if you notice any problems
    # th2 = -1*th2

    #Stuff for calculating th2
    k1 = l1 + l2*math.cos(th2)
    k2 = l2*math.sin(th2)
    r  = (k1**2 + k2**2)**0.5
    gamma = math.atan2(k2,k1)
    #calculate th1
    th1 = math.atan2(y,x) - gamma

    return abs(math.degrees(th1)), -math.degrees(th2)

#--------------------------------------------------------

class Point3D():
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, add):
        return Point2D(self.x + add.x, self.y + add.y, self.z + add.z)

    def __str__(self):
        return(self.x, self.y, self.z)


#IK for two links plus the base drum
def invkin3(point3d, angleMode=DEGREES):
    """Returns the angles of the first two links and
     the base drum in the robotic arm as a list.
    returns -> (th0, th1, th2)

    x - The x coordinate of the effector
    y - The y coordinate of the effector
    z - The z coordinate of the effector
    angleMode - tells the function to give the angle in
                degrees/radians. Default is degrees
    output:
    th0 - angle of the base motor
    th1 - angle of the first link w.r.t ground
    th2 - angle of the second link w.r.t the first"""
    x, y, z = point3d

    th0 = math.atan2(z,x)
    x = (x**2 + z**2)**0.5
    #stuff for calculating th2
    r_2 = x * x+ y * y
    l_sq = l1 * l1 + l2 * l2
    term2 = (r_2 - l_sq)/(2*l1*l2)
    term1 = ((1 - term2**2)**0.5)*-1
    #calculate th2
    th2 = math.atan2(term1, term2)
    #optional line. Comment this one out if you 
    #notice any problems
    th2 = -1*th2

    #Stuff for calculating th2
    k1 = l1 + l2*math.cos(th2)
    k2 = l2*math.sin(th2)
    r  = (k1**2 + k2**2)**0.5
    gamma = math.atan2(k2,k1)
    #calculate th1
    th1 = math.atan2(y,x) - gamma


    if(angleMode == RADIANS):
        return th0, th1, th2
    else:
        return math.degrees(th0), math.degrees(th1),\
            math.degrees(th2)


def distance3(x1, y1, z1, x2, y2, z2):
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1
    return dx*dx + dy*dy + dz*dz


# test >>>
# print(math.radians(180 / math.pi)) # def 1 rad: 360 / 2pi
# math.degrees(math.pi) # > 180.0
# print(cart2polar(polar2chart(1,90)[0],polar2cart(1,90)[1]))
