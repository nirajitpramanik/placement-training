from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def build_tree(self, arr):
        if not arr:
            return
        self.root = Node(arr[0])
        for val in arr[1:]:
            self._insert(self.root, val)

    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(node.right, val)

    def level_order(self):
        if not self.root:
            return []
        result = []
        queue = deque([self.root])
        while queue:
            level_values = []
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                if node:
                    level_values.append(node.val)
                    queue.append(node.left if node.left else None)
                    queue.append(node.right if node.right else None)
                else:
                    level_values.append(-1)
            if any(val != -1 for val in level_values):
                result.extend(level_values)
        return result

if __name__ == "__main__":
    tests = int(input())
    for i in range(tests):
        arr = [int(i) for i in input().split()]
        
        dummy = arr.copy()
        while dummy and dummy[-1] == -1:
            dummy.pop()
            
        bt = BST()
        bt.build_tree([val for val in arr if val != -1]) 
        
        arr2 = bt.level_order()
        while arr2 and arr2[-1] == -1:
            arr2.pop()
            
        if arr2 == dummy:
            print('true')
        else:
            print('false')
