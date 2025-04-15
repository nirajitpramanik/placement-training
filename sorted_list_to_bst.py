class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
        
    def build_tree(self, sorted_list):
        self.root = self._build_balanced_bst(sorted_list, 0, len(sorted_list) - 1)
        return self.root
    
    def _build_balanced_bst(self, sorted_list, start, end):
        if start > end:
            return None
        
        if ((end - start + 1) % 2 == 0):
            mid = ((start + end) // 2) + 1
        else:
            mid = (start + end) // 2

        node = Node(sorted_list[mid])
        
        node.left = self._build_balanced_bst(sorted_list, start, mid - 1)
        node.right = self._build_balanced_bst(sorted_list, mid + 1, end)
        
        return node
    
    def preorder_traversal(self, node):
        if not node:
            return []
        
        result = []
        result.append(str(node.val))
        result.extend(self.preorder_traversal(node.left))
        result.extend(self.preorder_traversal(node.right))
        
        return result

if __name__ == "__main__":
    input_list = list(map(int, input().split()))
    
    bst = BST()
    bst.build_tree(input_list)
    
    preorder = bst.preorder_traversal(bst.root)
    
    print(" ".join(preorder))
