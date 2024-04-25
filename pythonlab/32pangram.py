# Assignment 32
# Write a program to implement a pangram checker

def pangramchecker(a):
    flag = True
    for char in "abcdefghijklmnopqrstuvwxyz":
        if char not in a:
            flag = False
            break
    return flag

def main():
    string = input("Enter a word: ")
    print(pangramchecker(string))

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()