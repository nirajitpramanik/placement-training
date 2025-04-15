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

def sum_root_to_leaf(root, current_sum=0):
    if not root:
        return 0
    
    current_sum = current_sum * 10 + root.val
    
    if not root.left and not root.right:
        return current_sum
    
    return sum_root_to_leaf(root.left, current_sum) + sum_root_to_leaf(root.right, current_sum)

if __name__ == "__main__":
    input_str = input().strip().split()
    
    arr = ["N" if x == "N" else int(x) for x in input_str]
    
    root = build_tree(arr)
    
    result = sum_root_to_leaf(root)
    print(result)
