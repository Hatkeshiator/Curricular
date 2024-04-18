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
