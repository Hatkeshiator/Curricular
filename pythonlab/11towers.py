# Assignment 11
# copy the Towers of Hanoi algorithm given below

def print_move(fr, to):
    fr, to = str(fr), str(to)
    print('move from ' + fr + ' to ' + to)
    return

def towers(n, fr, to, spare):
    if n == 1:
        print_move(fr,to)
    else:
        towers(n-1,fr,spare,to)
        towers(1,fr,to,spare)
        towers(n-1,spare,to,fr)
    return # note that the value returned here is None

# Copy the improved towers of Hanoi algorithm

def Towers(n,fr,to,spare):
    if n==1:
        print_move(fr,to)
        return
    Towers(n-1,fr,spare,to)
    print_move(fr,to)
    Towers(n-1,spare,to,fr)

def main():
    n = int(input("Enter your number here: "))
    print("Assume the pole the stack currently is called 'start', and the other two are called 'end' and 'spare'. To move the stack from 'start' to 'end', do the following:")
    Towers(n, "'start'", "'end'", "'spare'")
    print("The stack is moved from 'start' to 'end.'")

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()
