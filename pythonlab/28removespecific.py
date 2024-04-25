# Assignment 28
# Write a program that prints the input list after removing the elements at indices 0, 2, 4, and 5

def remove_specific(l, indices = [0, 2, 4, 5]):
    return [l[i] for i in range(len(l)) if i not in indices]

def main():
    mylist = input("Enter a list of space separated values: ").split()
    indices = input("Enter the indices to remove: ").split()
    indices = [int(indx) for indx in indices]
    print(remove_specific(mylist, indices))

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()