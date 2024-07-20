from threading import Event

class Foo:
    def __init__(self):
        self.first_event = Event()
        self.second_event = Event()
        self.third_event = Event()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_event.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.first_event.wait()
        printSecond()
        self.second_event.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.second_event.wait()
        printThird()
            