# Assignment 9, part 2
# Write a program that checks if a given text input is a palindrome or not.
# A palindrome (like racecar) is spelled identically forwards as well as backwards.

#string = ["li", "ma", "di", "ga", "ma", "ma", "ga", "di", "ma", "li"]
def main():
    string = input("enter your string: ")
    if string == string[::-1]:
        print(string, "is a palindrome")
    else:
        print(string, "is not a palindrome; its reverse is", string[::-1])

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()
