string=input("Enter the String:")
revStr=""
stack=[]
for i in string:
    stack.append(i)
while len(stack) != 0:
    revStr+=stack.pop()
print("Reversed String is",revStr)
if string==revStr:
    print("String is Palindrome")
else:
    print("String is not Palindrome")
