from queue import Queue

class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x):
        self.queue1.put(x)

    def pop(self):
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        top_element = self.queue1.get()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element

    def top(self):
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        top_element = self.queue1.queue[0]
        self.queue2.put(self.queue1.get())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_element

    def empty(self):
        return self.queue1.empty() and self.queue2.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()