# Assignment 22
# Write a program to count the number of odd and even numbers in a list

def oddeven(l):
    oddnumbers = evennumbers = 0
    for x in l:
        isodd = x % 2
        if isodd == 1:
            oddnumbers += 1
        if isodd == 0:
            evennumbers += 1
    return (oddnumbers, evennumbers)

def main():
    mylist = input("Enter a list of space separated integers: ").split()
    mylist = [int(i) for i in mylist]
    print(oddeven(mylist))

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()
