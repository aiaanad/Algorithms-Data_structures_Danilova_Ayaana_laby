# Declaration of Doubly Linked List
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class Stack:
    def __init__(self):
        self.start = self.top = None

    # Check if stack is empty
    def isEmpty(self):
        if self.start:
            return False
        return True

    # pushes element onto stack
    def push(self, element):
        newP = Node(element)
        if self.start is None:
            self.start = self.top = newP
            return
        newP.prev = self.top
        self.top.next = newP
        self.top = newP

    # Pops top element from stack
    def pop(self):
        if self.isEmpty():
            print('List is Empty')
            return
        self.top = self.top.prev
        if self.top is not None:
            self.top.next = None

    # Prints the stack
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
