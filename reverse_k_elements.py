class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None
        self.Previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.Next = node
            node.Previous = self.tail
            self.tail = node

    def reverse_add(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.Previous = node
            node.Next = self.head
            self.head = node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.Next
        print()

    def print_reverse(self):
        current = self.tail
        while current:
            print(current.data, end=' ')
            current = current.Previous
        print()

def reverse_by_groups(linked_list, k):
    outputll = LinkedList()
    node = linked_list.head

    while node:
        count = 0
        temp = node
        newll = LinkedList()

        next_group_start = None

        while temp and count < k:
            newll.reverse_add(temp.data)
            temp = temp.Next
            count += 1
        next_group_start = temp

        new_node = newll.head
        
        if count < k:
            new_node = newll.tail
            
            while new_node:
                outputll.add_node(new_node.data)
                new_node = new_node.Previous
        else:
            while new_node:
                outputll.add_node(new_node.data)
                new_node = new_node.Next

        node = next_group_start

    return outputll

if __name__ == "__main__":
    linked_list = LinkedList()

    data = [int(i) for i in input().split()]
    k = int(input())

    for val in data:
        linked_list.add_node(val)

    reversed_grouped_ll = reverse_by_groups(linked_list, k)

    reversed_grouped_ll.print_list()
