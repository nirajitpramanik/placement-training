from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr):
    if not arr or arr[0] == "N":
        return None
    
    root = Node(int(arr[0]))
    queue = deque([root])
    i = 1
    
    while queue and i < len(arr):
        current = queue.popleft()
        
        if i < len(arr) and arr[i] != "N":
            current.left = Node(int(arr[i]))
            queue.append(current.left)
        i += 1
        
        if i < len(arr) and arr[i] != "N":
            current.right = Node(int(arr[i]))  
            queue.append(current.right)
        i += 1
    
    return root

def inorder_traversal(root):
    result = []
    
    def inorder(node):
        if not node:
            return
        
        inorder(node.left)
        result.append(node.val)
        inorder(node.right)
    
    inorder(root)
    return result

def kth_smallest(root, k):
    count = [0]  
    result = [None]
    
    def inorder(node):
        if not node or result[0] is not None:
            return
        
        inorder(node.left)
        
        count[0] += 1
        if count[0] == k:
            result[0] = node.val
            return
        
        inorder(node.right)
    
    inorder(root)
    return result[0]

if __name__ == "__main__":
    input_str = input().strip().split()
    k = int(input().strip())
    
    arr = ["N" if x == "N" else int(x) for x in input_str]
    
    root = build_tree(arr)
    
    result = kth_smallest(root, k)
    print(result)
