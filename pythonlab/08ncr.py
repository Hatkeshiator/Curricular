# Assignment 8
# Write a program to implement n C r and n P r functions.
# Choose/Combination operator n C r tells you how many subsets of a set with cardinality n have cardinality r i.e. how many "combinations" of cardinality r you can make out of it. the formula for it is (n!/((r!)((n-r)!)))
# n P r refers to permutations. For instance, {1,3,2} == {1,2,3}, but (1,3,2) != (1,2,3). There are thus r! more permutations of something than combinations (as there are r! unique ways to arrange r elements)

def factorial(x):
    result = 1
    for i in range(x):
        result *= (i+1)
    return result

def c(n,r):
    # by formula
    result = factorial(n) // (factorial(r) * factorial(n-r))
    return result

def p(n,r):
    # also by formula
    result = factorial(n) // factorial(n-r)
    return result

def main():
    num1, num2 = int(input("Enter first number: ")), int(input("Enter second number: "))
    print("n C r = ", c(num1, num2), "n P r = ", p(num1, num2))

if __name__ == '__main__':
    print("Written by Varad Kinjal Dixit, 23BBT035\n")
    main()
