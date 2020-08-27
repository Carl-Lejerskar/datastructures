class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        node = self.head

        while (node):
            print(node.value)
            node = node.next
    
    def insertHead(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        
    def append(self, value):
        node = Node(value)
        current = self.head

        while(current):
            prev = current 
            current = current.next
        
        prev.next = node 
    
    def delete(self, index):
        i = 0
        current = self.head
        previous = None

        while i < index:
            previous = current
            current = current.next

        if previous == None:    #If at the head of the list 
            self.head = current.next
        else:
            previous.next = current.next

if __name__ == "__main__":

    ll = LinkedList()       #Initialize a linked list
    ll.head = Node(1)       #Set the head of the linked list

    second = Node(2)        #Make two more nodes
    third = Node(3)

    ll.head.next = second   #Chain the nodes
    second.next = third
    
    ll.print()              #Print the values (Should return 1, 2, 3)

    ll.insertHead(0)        #Insert a node with value 0 at the head of the linked list

    ll.print()              #Print the values (Should return 0, 1, 2, 3)

    ll.append(4)            #Append a node with value 4 
                        
    ll.print()              #Print the values (Should return 0, 1, 2, 3, 4)

    ll.delete(0)            #Delete the first element

    ll.print()              #Print the values (Should return 1, 2, 3, 4)

    ll.delete(3)            #Delete the last element

    ll.print()              #Print the values (Shold return 1, 2, 3)
