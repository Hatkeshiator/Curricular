# Assignment 24
# Write a program to remove duplicate elements from a list

def removeduplicates(l):
    for x in reversed(range(len(l))):
        if l[x] in l[:x]:
            del l[x]
    return l

def main():
    mylist = input("Enter a list of space separated values: ").split()
    print(removeduplicates(mylist))

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()