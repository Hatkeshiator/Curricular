# blah blah print a triangle that has alternating lettter and number lines and the letter lines reset and the number ones don't
# eg
# 1
# A B
# 2 3 4
# A B C D
# 5 6 7 8 9

def numbline(x):
    for y in range((x-1)**2, x ** 2):
        print(y+1,end=' ')
    print('')

def letline(x):
    letters = x * 2
    if letters >= 26:
        print("ABCDEFGHIJKLMNOPQRSTUVWXYZ " * (letters // 26), end='')
    print("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:letters%26])

def my_tri(lines):
    string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    i = 1
    for x in range(lines):
        if x % 2 == 0:
            #numbline(i)
            print(list(range((i-1)**2, i**2)))
        else:
            letline(i)
            i += 1
    return

b = int(input("How many lines "))
my_tri(b)
