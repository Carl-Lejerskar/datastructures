class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def print(self):
        node = self.head

        while (node):
            print(node.value)
            node = node.next

    def printBackwards(self):
        node = self.last
        while (node):
            print(node.value)
            node = node.prev
    
    def push(self, value):
        node = Node(value)
        node.next = self.head
        node.prev = None
        if self.head is not None:
            self.head.prev = node
        self.head = node
#    def append(self, value):
           
#    def delete(self, index):
    
if __name__ == "__main__":
    dll = LinkedList()
    c = Node(2)
    
    dll.head = c
    dll.push(1)
    dll.push(0)

    dll.print()


