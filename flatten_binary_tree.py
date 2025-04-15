from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    if not root:
        return None
    
    flatten(root.left)
    flatten(root.right)
    
    if root.left:
        old_right = root.right
        
        root.right = root.left
        root.left = None  
        
        current = root.right
        while current.right:
            current = current.right
        
        current.right = old_right
    
    return root

def build_tree(arr):
    if not arr or len(arr) == 0 or arr[0] == 'N':
        return None
    
    root = Node(int(arr[0]))
    queue = deque([root])
    i = 1
    
    while queue and i < len(arr):
        current = queue.popleft()
        
        if i < len(arr):
            if arr[i] != 'N':
                current.left = Node(int(arr[i]))
                queue.append(current.left)
            i += 1
        
        if i < len(arr):
            if arr[i] != 'N':
                current.right = Node(int(arr[i]))
                queue.append(current.right)
            i += 1
    
    return root

def print_level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append('N')
    
    while result and result[-1] == 'N':
        result.pop()
        
    return result

def print_flattened_tree(root):
    result = []
    current = root
    while current:
        result.append(str(current.val))
        current = current.right
    return result

if __name__ == "__main__":
    input_str = input().strip()
    arr = [char for char in input_str.split()]
    
    root = build_tree(arr)
    
    flattened_root = flatten(root)
    flattened = print_flattened_tree(flattened_root)
    print(" ".join(flattened))
