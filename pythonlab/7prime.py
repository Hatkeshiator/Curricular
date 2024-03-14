# Write a program to check if a number is prime or not

def isprime(num):
    prime = True
    if (num % 2 == 0 and num != 2) or num == 1:
        prime = False
    for x in range(3, 1 + int(num ** (1/2)), 2):
        if num % x == 0:
            prime = False
    return prime

def primesto(num):
    result = []
    for x in range(num+1):
        if isprime(x):
            result.append(x)
    return result

def primesto_(x):
    return [k for k in range(x+1) if isprime(k)]
