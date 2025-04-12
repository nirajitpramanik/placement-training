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

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.Next
        print()
        
def reorder_list(linked_list):
    output = LinkedList()
    
    node1 = linked_list.head
    node2 = linked_list.tail
    
    while node1 != node2 and node1.Previous != node2:  
        output.add_node(node1.data)
        output.add_node(node2.data)
        
        node1 = node1.Next 
        node2 = node2.Previous  
   
    if node1 == node2:
        output.add_node(node1.data)
        
    return output

if __name__ == "__main__":
    linked_list = LinkedList()

    data = [int(i) for i in input().split()]
    
    for i in data:
        linked_list.add_node(i)

    outputll = reorder_list(linked_list)
    
    outputll.print_list()
