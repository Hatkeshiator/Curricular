def minmax(l):
    max = min = l[0]
    for x in l:
        if x > max:
            max = x
        if x < min:
            min = x
    return [min, max]

l = []
numbers = 15
for x in range(numbers):
    l.append(int(input(f"Enter number {x+1}: ")))

print(minmax(l))
