from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(arr):
    if not arr or arr[0] == -1:
        return None
    
    root = Node(arr[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(arr):
        current = queue.popleft()
        
        if i < len(arr) and arr[i] != -1:
            current.left = Node(arr[i])
            queue.append(current.left)
        i += 1
        
        if i < len(arr) and arr[i] != -1:
            current.right = Node(arr[i])
            queue.append(current.right)
        i += 1
    
    return root

def find_lca(root, x, y):
    if root is None:
        return None
    
    if root.val == x or root.val == y:
        return root
        
    left_lca = find_lca(root.left, x, y)
    right_lca = find_lca(root.right, x, y)
    
    if left_lca and right_lca:
        return root
    
    return left_lca if left_lca else right_lca

if __name__ == "__main__":
    arr = list(map(int, input().strip().split()))
    x, y = map(int, input().strip().split())

    root = build_tree(arr)
    
    lca_node = find_lca(root, x, y)
    
    if lca_node:
        print(lca_node.val)
