from threading import Event

class FooBar:
    def __init__(self, n):
        self.n = n
        self.first_event = Event()
        self.second_event = Event()
        self.first_event.set()
        


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            # printFoo() outputs "foo". Do not change or remove this line.
            self.first_event.wait()
            printFoo()
            self.first_event.clear()
            self.second_event.set()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.second_event.wait()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.second_event.clear()
            self.first_event.set()