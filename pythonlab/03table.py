# Assignment 3
# Write a program to output the times table of a number.

def make_table(number,upto):
    for x in range(upto):
        print(number,"*",x+1,"=\t",number*(x+1))

def main():
    a = int(input("Number to multiply: "))
    b = int(input("Times tables up to: "))

    make_table(a,b)

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()
