class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,val):
        if len(self.queue) == 5:
            return "Queue Overflow"
        else:
            self.queue.append(val)
            return ("Enqueued Element", val)
    def dequeue(self):
        if not self.queue:
            return "Queue Underflow"
        else:
            return self.queue.pop(0)
    def front (self):
        if not self.queue:
            return "Queue Underflow"
        else:
            return self.queue[0]
    def rear (self):
        if not self.queue:
            return "Queue Underflow"
        else:
            return self.queue[-1]
queueObj = Queue()
print(queueObj.front())
ele = input("Enter elements to enqueue: ").split()
for i in ele:
    print(queueObj.enqueue(i))
    print(queueObj.queue)