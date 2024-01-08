class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class FlipList:
    def __init__(self):
        self.front = None
        self.back = None

    def push_first(self, x):
        uusiAlkio = Node(x)
        if not self.front:
            self.front = uusiAlkio
            self.back = uusiAlkio
        else:
            uusiAlkio.next = self.front
            self.front.prev = uusiAlkio
            self.front = uusiAlkio

    def push_last(self, x):
        uusiAlkio = Node(x)
        if not self.back:
            self.front = uusiAlkio
            self.back = uusiAlkio
        else:
            uusiAlkio.prev = self.back
            self.back.next = uusiAlkio
            self.back = uusiAlkio

    def pop_first(self):
        if not self.front:
            return None
        value = self.front.value
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.back = None
        return value

    def pop_last(self):
        if not self.back:
            return None
        value = self.back.value
        self.back = self.back.prev
        if self.back:
            self.back.next = None
        else:
            self.front = None
        return value

    def flip(self):
        self.front, self.back = self.back, self.front

if __name__ == "__main__":
    f = FlipList()
    f.push_last(1)
    f.push_last(5)
    f.push_last(3)
    f.flip()
    print(f.pop_last())
    print(f.pop_last())
    print(f.pop_last())