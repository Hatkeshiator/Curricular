# adds one to duplicate count for every *repeated* occurence of an element
def duplicount(l):
    duplicates = 0
    for i in range(len(l)):
        if l[i] in l[:i]:
            duplicates += 1
    print ("there are", duplicates, "duplicate items")


# adds one to duplicate count for every *unique* duplicate element
def Duplicount(l):
    duplicates = []
    for i in range(len(l)):
        if l[i] in l[:i] and l[i] not in duplicates:
            duplicates.append(l[i])
    print ("there are", len(duplicates), "duplicate items (", duplicates, ")")

# simply counts every element that is present elsewhere in the list
def _duplicount(l):
    duplicates = 0
    for i in range(len(l)):
        l2 = l[:i] + l[i+1:]
        if l[i] in l2:
            duplicates += 1
    print ("there are", duplicates, "duplicate items")
