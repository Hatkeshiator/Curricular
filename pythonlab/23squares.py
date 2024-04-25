# Assignment 23
# Write a function that takes a list of numbers and returns a new list with the square of each number. Write a list comprehension that does the same thing.

def squareeach(l):
    result = []
    for x in range(len(l)):
        result.append(l[x] ** 2)
    return result

def squarecomp(l):
    return [x ** 2 for x in l]

def squareeven(l):
    return [x ** 2 for x in l if x % 2 == 0]

def main():
    mylist = input("Enter a list of space separated integers: ").split()
    mylist = [int(i) for i in mylist]
    print(squareeven(mylist))

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()
