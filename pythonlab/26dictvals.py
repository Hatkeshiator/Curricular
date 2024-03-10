# Write a program that takes a list as input and returns a dictionary containing key-value pairs of {key_a: [a1, a2 ,a3, ... an], key_b: [b1, b2, b3 ... bm]} for n instances of the value key_a in original list, and m instances of key_b.

def dictvals(l):
    d = {}
    # iterate over L
    for i in l:
        # add the value to the dictionary if it doesn't exist and give it a value of [i]
        if i not in d:
            d[i] = [i]
        # if the value exists, append the value to the list
        else:
            d[i].append(i)
    return d