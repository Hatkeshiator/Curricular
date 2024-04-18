# Write a program that checks if a number is an armstrong number or not.
# An Armstrong number is one whose value is equal to the sum of its digits, each raised to the mth power, where m is the number of digits in the number.

def armstrong(number):
    result = 0
    # with a string, we can iterate over each digit individually
    numberstring = str(number)
    for x in numberstring:
        result += int(x) ** len(numberstring)
    # is result the same as our initial number?
    final_result = (result == number) and (number != 0) # 0 is not considered an armstrong number (by the OEIS), even though 0^1 = 0.
    return final_result
# optional: write an algorithm that checks numbers up to a desired value

def interesting(ran):
    nums = []
    i = 0
    for x in range(ran):
        if armstrong(x):
            i += 1
            nums.append(x)
    for x in range(len(nums)):
        if x != len(nums) - 1:
            print(nums[x], end=', ')
        else:
            print(nums[x])
    return 

def main():
    a = int(input("Enter your number: "))
    print(armstrong(a))
