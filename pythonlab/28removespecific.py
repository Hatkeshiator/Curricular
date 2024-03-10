# Write a program that prints the input list after removing the elements at indices 0, 2, 4, and 5

def remove_specific(l, indices = [0, 2, 4, 5]):
    return [l[i] for i in range(len(l)) if i not in indices]