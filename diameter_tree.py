class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(s):
    if not s:
        return None
    
    values = s.split()
    
    if values[0] == 'N':
        return None
    
    root = TreeNode(int(values[0]))
    
    queue = [root]
    i = 1
    
    while queue and i < len(values):
        node = queue.pop(0)
        
        if i < len(values) and values[i] != 'N':
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] != 'N':
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1
    
    return root

def diameter_tree(root):
    max_diameter = [0] 
    def height(node):
        if not node:
            return 0
        
        left_height = height(node.left)
        right_height = height(node.right)
        
        max_diameter[0] = max(max_diameter[0], left_height + right_height)
        
        return max(left_height, right_height) + 1
    
    height(root)
    return max_diameter[0] + 1

if __name__ == "__main__":
    s = input().strip()
    root = build_tree(s)
    print(diameter_tree(root))
