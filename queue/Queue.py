class queue:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.insert(0, value)

    def dequeue(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def print(self):
        print(self.data)
