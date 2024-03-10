# Write a program that takes two lists as inputs and returns True if they have at least one common element and False otherwise.

def common(l1, l2):
    result = False
    for i in l1:
        if i in l2:
            result = True
    return result