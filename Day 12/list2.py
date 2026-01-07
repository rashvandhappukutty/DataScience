class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
newNode = Node(10)
newNode_1 = Node(20)
newNode_2 = Node(30)

newNode.next = newNode_1
newNode_1.next = newNode_2

current = newNode
while current is not None:
    print(current.data, end="-->" if current.next is not None else " --> None")
    current = current.next

print("\n List is printed")            
