def oddeven(l):
    oddnumbers = evennumbers = 0
    for x in l:
        isodd = x % 2
        if isodd == 1:
            oddnumbers += 1
        if isodd == 0:
            evennumbers += 1
    return (oddnumbers, evennumbers)
