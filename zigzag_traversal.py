class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Stack:
    def __init__(self):
        self.items = []
        self.top = -1
        
    def push(self, val):
        self.items.append(val)
        self.top += 1
        
    def pop(self):
        self.top -= 1
        return self.items.pop()
        
    def peek(self):
        return self.items[self.top]

class BinaryTree:
    def __init__(self):
        self.root = None
        self.queue = []
        
    def build_tree(self, arr):
        if not arr:
            return None
        self.root = Node(arr[0])
        self.queue.append(self.root)
        i = 1
        while i < len(arr):
            node = self.queue.pop(0)
            if node.left is None:
                node.left = Node(arr[i])
                self.queue.append(node.left)
                i += 1
            if i < len(arr) and node.right is None:
                node.right = Node(arr[i])
                self.queue.append(node.right)
                i += 1
                
        return self.root

class ZigZagTraversal:
    def __init__(self):
        self.current_level = Stack()
        self.next_level = Stack()
        self.result = []
        
    def traverse(self, root):
        if not root:
            return []
        
        self.current_level.push(root)
        left_to_right = True
        level_vals = []
        
        while self.current_level.items:
            current_node = self.current_level.pop()
            level_vals.append(current_node.val)
            
            if left_to_right:
                if current_node.left:
                    self.next_level.push(current_node.left)
                if current_node.right:
                    self.next_level.push(current_node.right)
            else:
                if current_node.right:
                    self.next_level.push(current_node.right)
                if current_node.left:
                    self.next_level.push(current_node.left)
            
            if not self.current_level.items:
                self.result.extend(level_vals)
                level_vals = []
                self.current_level, self.next_level = self.next_level, self.current_level
                left_to_right = not left_to_right
                
        return self.result

if __name__ == "__main__":
    inp = [int(i) for i in input().split()]
    bt = BinaryTree()
    root = bt.build_tree(inp)
    
    zz = ZigZagTraversal()
    result = zz.traverse(root)
    
    out = ""
    
    for i in result:
        out += f"{i} "
        
    print(out.strip())
