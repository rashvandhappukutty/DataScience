class Stack:
    def __init__(self, max_size=5):
        self.stack = []
        self.max_size = max_size
    
    def push(self, data):
        if len(self.stack) >= self.max_size:
            return "Stack Overflow"
        self.stack.append(data)
        return f"Pushed: {data}"
    
    def pop(self):
        if not self.stack:
            return "Stack Underflow"
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def peek(self):
        if not self.stack:
            return "Stack is Underflow"
        else:
            return self.stack[-1]

stackObj = Stack(5)
elements = [5, 10, 15, 20, 25, 30]

for elem in elements:
    stackObj.push(elem)
    print(stackObj.stack)