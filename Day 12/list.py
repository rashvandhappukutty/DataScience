class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

newNode = Node(10)
newNode_1 = Node(20)
newNode_2 = Node(30)

newNode.Next = newNode_1
newNode_1.Next = newNode_2

print(newNode.data,end=" ")
print(newNode.Next.data,end=" ")
print(newNode.Next.Next.data,end=" ")
print("None")