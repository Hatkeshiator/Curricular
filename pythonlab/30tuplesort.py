# Write a program to sort a tuple of tuples by the *second* item of those tuples.
# Example input: (('a', 34), ('b', 23), ('c', 67), ('d', 100), ('e', 0))

#def sort_tuples(t):
#    return sorted(t, key = lambda x: x[1])

def sort_tuples(t):
    l = []
    for i in t:
        l.append(i)
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i][1] < l[j][1]:
                l[i], l[j] = l[j], l[i]
    return tuple(l)
