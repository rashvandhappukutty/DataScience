def balancedParathesis(paran):
    stack = []
    pair = {')': '(', '}': '{', ']': '['}
    
    for char in paran:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != pair[char]:
                return False
    return len(stack) == 0

paran = input("Enter the Parentheses: ")
if balancedParathesis(paran):
    print("Balanced")
else:
    print("Not Balanced")