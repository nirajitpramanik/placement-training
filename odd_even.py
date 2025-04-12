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

        if self.head == None:
            self.head = node
            self.tail = node
            self.head.next = self.tail

        else:
            self.tail.next = node
            self.tail = node

    def print_odd_even(self):
        output = ""
        even_head = self.head
        odd_head = self.head

        while even_head:
            if even_head.val % 2 == 0:
                output += f"{str(even_head.val)} "

            even_head = even_head.next

        while odd_head:
            if odd_head.val % 2 != 0:
                output += f"{str(odd_head.val)} "

            odd_head = odd_head.next

        print(output.strip())

if __name__ == "__main__":
    linked_list = LinkedList()

    data = [int(i) for i in input().split()]

    for num in data:
        linked_list.add_node(num)

    linked_list.print_odd_even()
