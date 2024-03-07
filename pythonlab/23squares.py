def squareeach(l):
    result = []
    for x in range(len(l)):
        result.append(l[x] ** 2)
    return result

def squarecomp(l):
    return [x ** 2 for x in l]

def squareeven(l):
    return [x ** 2 for x in l if x % 2 == 0]
