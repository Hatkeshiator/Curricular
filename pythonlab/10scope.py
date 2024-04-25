# Assignment 10
# Write a program to understand the scope of a function

def g(x):
    def h():
        #print('x in h =', x) #-> NameError
        x = 'abc'
        #print('x after h =', x) #-> 'abc'
    #print('before g, x =', x) #-> input value
    x = x + 1
    print('in g(x): x =', x) #-> input value + 1
    h() # doesn't do anything because the x in h is treated differently from the x in g
    # this is called scope
    return x

def main():
    x = int(input('what is x '))
    z = g(x)
    print(z)

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()
