class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Stack:
    def __init__(self):
        self.start = None
        self.top = None

    def isEmpty(self):
        if self.start:
            return False
        return True

    def push(self, element):
        newP = Node(element)
        if self.start is None:
            self.start = self.top = newP
            return
        newP.prev = self.top
        self.top.next = newP
        self.top = newP

    def pop(self):
        if self.isEmpty():
            return None
        popped_value = self.top
        if self.start == self.top:
            self.top = self.start = None
            return popped_value.val

        self.top = self.top.prev
        if self.top is not None:
            self.top.next = None
        return popped_value.val

    def printstack(self):
        if self.isEmpty():
            print('List is Empty')
            return
        curr = self.start
        print("Stack is :  ", end='')
        while curr is not None:
            print(curr.val, end=' ')
            curr = curr.next
        print()


if __name__ == "__main__":
    pass
