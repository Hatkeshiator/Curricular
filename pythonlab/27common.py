# Assignment 27
# Write a program that takes two lists as inputs and returns True if they have at least one common element and False otherwise.

def common(l1, l2):
    result = False
    for i in l1:
        if i in l2:
            result = True
    return result

def main():
    mylist1 = input("Enter a list of space separated values: ").split()
    mylist2 = input("Enter a list of space separated values: ").split()
    print(common(mylist1, mylist2))

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()