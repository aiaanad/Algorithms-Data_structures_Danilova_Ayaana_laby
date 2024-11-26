class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last.next.prev = self.last
            self.last = self.last.next

    def dequeue(self):
        if self.head is None:
            return None
        else:
            temp = self.head.data
            if self.last != self.head:
                self.head = self.head.next
            else:
                self.head = self.last = None
            return temp

    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    def isEmpty(self):
        if self.head == self.last and self.head is None:
            return True
        return False

    def __repr__(self):
        queue = ''
        temp = self.head
        while temp is not None:
            queue += str(temp.data)
            temp = temp.next
        return queue


if __name__ == "__main__":
    pass
