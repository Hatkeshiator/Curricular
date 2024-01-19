def cube_root(number):
    a = 0
    while a ** 3 < number:
        a += 1
    if a ** 3 == number:
        ret = f"the cube root of {number} is {a}"
    else:
        ret = f"the cube root of {number} is between {a-1} and {a}"
    return ret

def main():
    a = int(input("Enter number: "))
    print(cube_root(a))
