# Write a program to output the times table of a number.

def make_table(number,upto):
    for x in range(upto):
       #print(f"{number} * {x+1} =\t{number * (x+1)}")
        print(number,"*",x+1,"=\t",number*(x+1))

a = int(input("Number to multiply: "))
b = int(input("Times tables up to: "))

make_table(a,b)
