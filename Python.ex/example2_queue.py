from queue import Queue

class MyQueue(Queue):
    def __repr__(self):
        return f"MyQueue(size={self.qsize()})"

    def __add__(self, item):
        self.put(item)
        return self


q = MyQueue()
q + 10
q + 20
print(q)
