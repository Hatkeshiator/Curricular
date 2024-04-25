# Assignment 13
# Write a program to import pi from math, and then use it to define area and circumference calculating functions

from math import pi

def area(r):
    a = pi * r ** 2
    return a

def circum(r):
    c = pi * r * 2
    return c

def main():
    r = int(input("Enter the radius of the circle: "))
    print("The area of the circle is:", area(r), "\nThe circumference is:", circum(r))

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()
