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

    llo.print_list()
        
if __name__ == "__main__":
    linked_list1 = LinkedList()
    linked_list2 = LinkedList()

    num1 = int(input())
    data1 = [int(i) for i in input().split()]
    for i in data1:
        linked_list1.add_node(i)

    num2 = int(input())
    data2 = [int(i) for i in input().split()]
    for i in data2:
        linked_list2.add_node(i)

    merge_lists(linked_list1, linked_list2)
