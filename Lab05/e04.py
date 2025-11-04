class DataStruct:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def is_empty(self):
        if len(self._items) == 0:
            return True
        else:
            return False

class Queue(DataStruct):
    def __init__(self):
        super().__init__()

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            print(f'Pop response: {None}')
            return None
        else:
            print(f'Pop response: {self._items.pop(0)}')
            return self._items.pop(0)

    def peek(self):
        if self.is_empty():
            print(f'Peek response: {None}')
            return None
        else:
            print(f'Peek response: {self._items[0]}')
            return self._items[0]

class Stack(DataStruct):
    def __init__(self):
        super().__init__()

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            print(f'Pop response: {None}')
            return None
        else:
            print(f'Pop response: {self._items.pop()}')
            return self._items.pop()

    def peek(self):
        if self.is_empty():
            print(f'Peek response: {None}')
            return None
        else:
            print(f'Peek response: {self._items[-1]}')
            return self._items[-1]

stiva = Stack()
stiva.push(20)
stiva.peek()
stiva.push(10)
stiva.peek()
stiva.push(0)
stiva.peek()
stiva.pop()

coada = Queue()
coada.push(0)
coada.peek()
coada.push(1)
coada.peek()
coada.push(2)
coada.peek()
coada.pop()
