# Write a program to import pi from math, and then use it to define area and circumference calculating functions

from math import pi

def area(r):
    a = pi * r ** 2
    return a

def circum(r):
    c = pi * r * 2
    return c
