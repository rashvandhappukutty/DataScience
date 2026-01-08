def evaluate_postfix(expression):
    stack = []
    
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            
            if char == '+':
                result = num1 + num2
            elif char == '-':
                result = num1 - num2
            elif char == '*':
                result = num1 * num2
            elif char == '/':
                result = num1 / num2
            else:
                raise ValueError(f"Unknown operator: {char}")
            
            stack.append(result)
    
    return stack[0]
expression = input().strip()
print(evaluate_postfix(expression))