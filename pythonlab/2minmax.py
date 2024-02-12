# Write a program that checks the maximum of three numbers, input from user.

def minnmax(p):
    maximum = minimum = p[0]
    for x in range(len(p)):
        if p[x] > maximum:
            maximum = p[x]
        if p[x] < minimum:
            minimum = p[x]
    return maximum, minimum

p = (int(input("Enter three numbers: ")), int(input()), int(input()))
r = minnmax(p)
print('maximum: ', r[0], '\tminimum: ', r[1])
