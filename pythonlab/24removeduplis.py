# Write a program to remove duplicate elements from a list

def removeduplicates(l):
    for x in reversed(range(len(l))):
        if l[x] in l[:x]:
            del l[x]
    return l
