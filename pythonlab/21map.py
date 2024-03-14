# Write a program to replace vowels in a string with special symbols of your choice
# (I chose 4, 3, 1, 0, 9 for a, e, i, o, u respectively)

def vowelreplace(inst):
    myst = ""
    for char in inst:
        if char == 'a' or char == 'A':
            myst += '4'
        elif char == 'e' or char == 'E':
            myst += '3'
        elif char == 'i' or char == 'I':
            myst += '1'
        elif char == 'o' or char == 'O':
            myst += '0'
        elif char == 'u' or char == 'U':
            myst += '9'
        else:
            myst += char
    print(myst)

def vowelreplace_(inst):
    ref1 = "AEIOUaeiou"
    ref2 = "4310943109"
    myst = ""
    for char in inst:
        if char in ref1:
            myst += ref2[ref1.index(char)]
        else:
            myst += char
    print(myst)


# better approach using map() (not yet taught(?))
def vowelmap(inst):
    def repl(char):
        result = char
        if char == 'a' or char == 'A':
            result = '4'
        elif char == 'e' or char == 'E':
            result = '3'
        elif char == 'i' or char == 'I':
            result = '1'
        elif char == 'o' or char == 'O':
            result = '0'
        elif char == 'u' or char == 'U':
            result = '9'
        return result
    myst = map(repl, inst)
    myst = list(myst)
    myst = ''.join(myst)
    return myst

def vowelmap_(inst):
    ref1 = "AEIOUaeiou"
    ref2 = "4310943109"
    def repl(char):
        if char in ref1:
            return ref2[ref1.index(char)]
        else:
            return char
    myst = map(repl, inst)
    myst = list(myst)
    myst = ''.join(myst)
    return myst