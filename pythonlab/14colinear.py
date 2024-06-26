# Assignment 14
# collinear = lying on the plane such that there exists a line that passes through all points

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

def iscollinear(x_1,y_1,x_2,y_2,x_3,y_3):
    x1tox2 = riorun(x_1,y_1,x_2,y_2)
    x2tox3 = riorun(x_2,y_2,x_3,y_3)
    collin_flag = False
    if x1tox2 == x2tox3:
        collin_flag = True
    return collin_flag

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\nUse the function iscollinear() to find if 3 points are collinear.")
