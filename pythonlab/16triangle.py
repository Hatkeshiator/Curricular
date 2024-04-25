# Assignment 16
# Write a program to print a triangle that has alternating lettter and number lines and the letter lines reset and the number ones don't

# eg
# 1
# A B
# 2 3 4
# A B C D
# 5 6 7 8 9

def letline(x):
    letters = x * 2
    if letters >= 26:
        print("ABCDEFGHIJKLMNOPQRSTUVWXYZ " * (letters // 26), end='')
    print("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:letters%26])

def my_tri(lines):
    i = 1
    for x in range(lines):
        print(list(range((i-1)**2, i**2)))
        letline(i)
        i += 1
    return

def main():
    b = int(input("How many lines "))
    my_tri(b)

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()
