def reverse(str):
    revStr=""
    stack=[]
    for i in str:
        stack.append(i)
    while len(stack) != 0:
        revStr+=stack.pop()
    return revStr
str=input("Enter the String:")
print("Reversed String is are :",reverse(str))