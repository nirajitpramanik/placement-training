class Node:
    def __init__(self, data):
        self.data = data
        self.Previous = None
        self.Next = None

class LinkedList:
    def __init__(self, length):
        self.length = length
        self.head = None
        self.tail = None

    def add_node(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
            self.head.Next = self.tail
            self.tail = node
            self.tail.Previous = self.head

        else:
            self.tail.Next = node
            node.Previous = self.tail
            self.tail = node

    def find_mid_node(self, mid):
        counter = 0
        node = self.head

        while (counter != mid):
            node = node.Next
            counter += 1

        return node

    def check_palindrome(self):
        if self.length % 2 != 0:
            mid = (self.length + 1) // 2

            mid_node = self.find_mid_node(mid - 1)
            lhs, rhs = "", ""

            node1 = self.head

            while (node1 != mid_node):
                lhs += str(node1.data)
                node1 = node1.Next

            node2 = self.tail

            while (node2 != mid_node):
                rhs += str(node2.data)
                node2 = node2.Previous
    
            return lhs == rhs

        else:
            mid = self.length // 2

            mid_node = self.find_mid_node(mid)
            lhs, rhs = f"{self.head.data}", f"{self.tail.data}"

            node1 = self.head

            while (node1 != mid_node.Previous):
                node1 = node1.Next
                lhs += str(node1.data)

            node2 = self.tail

            while (node2 != mid_node):
                node2 = node2.Previous
                rhs += str(node2.data)

            return lhs == rhs

if __name__ == "__main__":
    leng = int(input())
    nums = [int(i) for i in input().split()]

    linked_list = LinkedList(leng)

    for num in nums:
        linked_list.add_node(num)

    flag = linked_list.check_palindrome()

    if flag:
        print('true')
    else:
        print('false')
