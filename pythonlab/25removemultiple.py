# Assignment 25
# Write a program that removes all occurrences of any of a given list of values from a list.

def rem_all(l, torem):
    return [i for i in l if i not in torem]

def main():
    mylist = input("Enter a list of space separated values: ").split()
    rem = input("What to remove from your list?").split()
    print(rem_all(mylist, rem))

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()