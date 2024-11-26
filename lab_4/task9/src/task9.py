from lab_4.utils.utils import work
from pathlib import Path


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Clinic:
    def __init__(self):
        self.head = None
        self.last = None

    def new_patient(self, data):
        if self.head is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last.next.prev = self.last
            self.last = self.last.next

    def find_middle(self):
        if self.head is None:
            return None
        _l = self.head
        r = self.last
        while _l.data != r.data and _l.next.data != r.data:
            _l = _l.next
            r = r.prev
        return _l

    def get_certificate(self, data):
        if self.head is None:
            self.head = Node(data)
            self.last = self.head
        mid = self.find_middle()
        next_to_mid = mid.next
        mid.next = Node(data)
        mid.next.prev = mid
        mid.next.next = next_to_mid

    def go_doctor(self):
        if self.head is None:
            return None
        if self.head == self.last:
            patient = self.head
            self.head = self.last = None
            return patient.data

        patient = self.head
        self.head = self.head.next
        self.head.prev = None
        return patient.data

    def __repr__(self):
        queue = ''
        temp = self.head
        while temp is not None:
            queue += f' {temp.data}'
            temp = temp.next
        return queue


def main(n, *operations):
    ans = []
    q = Clinic()
    for action in operations:
        match action[0]:
            case '+':
                q.new_patient(action[1])
            case '*':
                q.get_certificate(action[1])
            case '-':
                ans += [q.go_doctor()]
    return ans


if __name__ == "__main__":
    work(Path(__file__), main)


