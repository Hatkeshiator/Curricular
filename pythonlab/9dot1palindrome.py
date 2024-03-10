# Write a program that checks if a number is a palindrome or not
# A palindrome is a number whose value is identical whether its digits are read from left to right or right to left (omitting trailing zeroes)

def ispal(number):
    temp = number
    result = 0
    while temp > 0:
        #print(temp, number, result)
        result *= 10
        result += temp % 10
        temp //= 10
    #print(temp, number, result)
    return result == number
