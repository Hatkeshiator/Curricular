# colinear = lying on the plane such that there exists a line that passes through all points

# eqn for a line is y = mx+c
# or more relevantly, that dy/dx is constant over the graph

# define a function that tells us the slope between two points

def riorun(x_1, y_1, x_2, y_2): # "RIse Over RUN"
    numerator = y_2 - y_1
    denominator = x_2 - x_1
    numerator, denominator = abs(numerator), abs(denominator)
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        result = 'vert' # vertical, since y changes but x remains constant
    return result

# define a function that tells us if three points are colinear

def iscolinear(x_1,y_1,x_2,y_2,x_3,y_3):
    x1tox2 = riorun(x_1,y_1,x_2,y_2)
    x2tox3 = riorun(x_2,y_2,x_3,y_3)
    colin_flag = False
    if x1tox2 == x2tox3:
        colin_flag = True
    return colin_flag

# define a function that tells us the area of the triangle formed by three points

def triangle_area(x_1,y_1,x_2,y_2,x_3,y_3):
    # I wrote this while sleep deprived and cannot remember why it le works
    area = 0.5 * abs((x_1-x_3)*(y_2-y_1) - (x_1-x_2)*(y_3-y_1))
    return area
