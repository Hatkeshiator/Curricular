# Write a program to implement matrix multiplication.

def matmul(a,b):

    r1 = len(a)
    c2 = len(b[0])

    if len(a[0]) != len(b):
        raise ValueError("bad value (matrix 1 columns should equal matrix 2 rows)")
    else:
        r2c1 = len(b)

    result = [[0 for x in range(c2)] for x in range(r1)]

    # print(result)

    for i in range(r1):
        for j in range(c2):
            for k in range(r2c1): # can just as well be range(len(a[0]))
                result[i][j] += a[i][k] * b[k][j]

    return result
