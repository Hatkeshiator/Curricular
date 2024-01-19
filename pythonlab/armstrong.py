def moms_spaghetti(number):
    digits = []
    number_as_string = str(number)
    for num in number_as_string:
        digits.append(int(num))
    result = 0
    for x in digits:
        result += x ** len(digits)
    final_result = result == (int(number_as_string))
    # handling [[specil]] case:
    if number_as_string == '0':
        final_result = False
    
    return final_result

def interesting(ran):
    nums = []
    i = 0
    for x in range(ran):
        if moms_spaghetti(x):
            i += 1
            nums.append(x)
    for x in range(len(nums)):
        if x == len(nums) - 1:
            print(nums[x])
        else:
            print(nums[x], end=', ')

def main():
    a = int(input("Enter your number: "))
    print(moms_spaghetti(a))
