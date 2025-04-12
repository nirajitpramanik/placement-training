class Node:
    def __init__(self, val):
        self.val = val
        self.Next = None
        self.Previous = None

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
            self.tail.Next = node
            node.Previous = self.tail
            self.tail = node

    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=' ')
            current = current.Next
        print()

    def sort_list(self):
        # First, extract all values from the linked list
        values = []
        current = self.head
        while current:
            values.append(current.val)
            current = current.Next

        # Sort the values
        values.sort()

        # Rebuild the list with sorted values
        self.head = None
        self.tail = None
        for val in values:
            self.add_node(val)

def merge_lists(ll1, ll2):
    llo = LinkedList()

    node1, node2 = ll1.head, ll2.head

    while node1 and node2:
        if node1.val < node2.val:
            llo.add_node(node1.val)
            node1 = node1.Next
        else:
            llo.add_node(node2.val)
            node2 = node2.Next

    while node1:
        llo.add_node(node1.val)
        node1 = node1.Next
    
    while node2:
        llo.add_node(node2.val)
        node2 = node2.Next

    return llo

if __name__ == "__main__":
    k = int(input())
    linked_list1 = LinkedList()

    leng1 = int(input())
    data1 = [int(i) for i in input().split()]
    data1.sort()  
    for i in data1:
        linked_list1.add_node(i)
    
    for _ in range(k - 1):
        leng2 = int(input())
        data2 = [int(i) for i in input().split()]
        data2.sort()
        
        linked_list2 = LinkedList()
        for i in data2:
            linked_list2.add_node(i)

        linked_list1 = merge_lists(linked_list1, linked_list2)
        
    linked_list1.print_list()
