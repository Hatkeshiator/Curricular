# Write a program to compute whether a given point is on a given circle or not

def oncircle(x,y,r):
    dsqr = x ** 2 + y ** 2
    if dsqr > r ** 2:
        l = "outside"
    elif dsqr < r ** 2:
        l = "inside"
    else:
        l = "on"
    print("The point lies", l, "the circle")
    
from math import sqrt

def newoncircle(x,y,r):
    dsqr = x ** 2 + y ** 2
    d = sqrt(dsqr)
    if d > r:
        l = "outside"
    elif d < r:
        l = "inside"
    else:
        l = "on"
    print("The point lies", l, "the circle")

# optional: in n dimensions

def On_Circle(p,c,r):
    #p = [point_x, point_y]
    #c = [center_x, center_y]
    #r = radius
    dimensions = len(p)
    sumofsqrs = 0
    # compute each delta(x) and square it
    for d in range(dimensions):
        p[d] -= c[d]
        sumofsqrs += p[d] ** 2

    distance = sqrt(sumofsqrs)
    if distance > r:
        l = 'outside'
    elif distance < r:
        l = 'inside'
    else:
        l = 'on'
    print("The point lies", l, "the circle")
    return
