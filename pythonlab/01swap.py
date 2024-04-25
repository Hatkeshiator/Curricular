# Assignment 1
# Write a program that asks input of two numbers from user, assigns them to two different variables, swaps the variables, and then prints them.
def main() -> None:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    print("Before swap: a =", num1, "b =", num2)
    num1, num2 = num2, num1
    print("After swap:  a =", num1, "b =", num2)

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()

