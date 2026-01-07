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
        if not self.stack:
            return "Stack is empty"
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def __str__(self):
        return str(self.stack)

stackObj = Stack(5)
elements = [5, 10, 15, 20, 25, 30, 35]

for elem in elements:
    stackObj.push(elem)
    print(stackObj.stack)