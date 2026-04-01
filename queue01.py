from collections import deque

class stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def add(self, data):
        while len(self.q1):
            self.q2.append(self.q1.popleft())

        self.q1.append(data)

        while len(self.q2):
            self.q1.append(self.q2.popleft())

    def pop(self):
        if not self.q1:
            print("underflow!!")
            return None
        return self.q1.popleft()

    def is_empty(self):
        return len(self.q1) == 0


if __name__ == "__main__":
    keys = [1, 2, 3, 4, 5]
    s = stack()

    for key in keys:
        s.add(key)

    while not s.is_empty():
        print(s.pop())

    print(s.pop())
