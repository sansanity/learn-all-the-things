from collections import deque

queue = deque()

class Queue:
    def __init(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.appendleft(value)
    
    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)