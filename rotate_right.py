class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_node(self, val):
        node = Node(val)
        
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def print_list(self):
        node = self.head
        while node:
            print(node.val, end=" ")
            node = node.next
        print()
    
    def rotate(self, k):
        if self.head is None or k == 0:
            return
        
        current = self.head
        length = 1
        while current.next:
            current = current.next
            length += 1
        
        k = k % length
        if k == 0:
            return
        
        current = self.head
        for _ in range(length - k - 1):
            current = current.next
        
        new_head = current.next
        current.next = None
        self.tail.next = self.head
        self.head = new_head
        self.tail = current


if __name__ == "__main__":
    data = [int(i) for i in input().split()]
    stopper = int(input())
    k = int(input())
    rotate = 2
    #int(input())
    
    linked_list = LinkedList()
    
    for i in data:
        linked_list.add_node(i)
    
    linked_list.rotate(rotate)
    
    linked_list.print_list()
