# Assignment 4, part 1
# Write a program to count the number of vowels in a given string

ref = "AEIOUaeiou"

def counter(string):
    count = 0
    for char in string:
        if char in ref:
            count += 1
    return count

def main():
    a = input("Enter your string: ")
    print(counter(a))

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()
