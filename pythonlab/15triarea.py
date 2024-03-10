# Write a program to check the area of a triangle given the cartesian coordinates of its vertices

def triangle_area(x_1,y_1,x_2,y_2,x_3,y_3):
    # imagine copying the triangle you have and rotating it by 180 degrees
    # now put like sides of the triangles over top of each other and deleting that side
    # this resultant shape is a parallelogram
    # the formula for the area of a paralellogram given three of its points is:
    area = (x_1-x_3)*(y_2-y_1) - (x_1-x_2)*(y_3-y_1)
    # but this value may be negative for certain coordinates, so we take modulus:
    area = abs(area)
    # and the triangle is, by definition, half of the parallelogram
    area /= 2
    return area