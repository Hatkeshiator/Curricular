# Assignment 2
# Write a program that checks the maximum of three numbers, input from user.

def minimax(p):
    maximum = minimum = p[0]
    for x in range(len(p)):
        if p[x] > maximum:
            maximum = p[x]
        if p[x] < minimum:
            minimum = p[x]
    return maximum, minimum


def main():
    p = (int(input("Enter three numbers: ")), int(input()), int(input()))
    r = minimax(p)
    print('maximum: ', r[0], '\tminimum: ', r[1])

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()


