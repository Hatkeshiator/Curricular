def make_table(number,upto):
    for x in range(upto):
        print(number,"*",x+1,"=",number*(x+1))
    return True

a = int(input("Number to multiply: "))
b = int(input("Times tables up to: "))

make_table(a,b)
