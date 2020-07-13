class Queue:
    def __init__(self):
        self.queue = []

    def eneque(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if not self.queue:
            print("nothing to dequeue")
            return
        return self.queue.pop(0)