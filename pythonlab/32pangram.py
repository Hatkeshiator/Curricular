# Write a program to implement a pangram checker

def pangramchecker(a):
    flag = True
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in a:
            flag = False
            break
    return flag
