class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree(arr):
    if arr[0] == 'N':
        return None
    root = Node(int(arr[0]))
    queue = [root]
    i = 1
    while i < len(arr):
        curr = queue.pop(0)
        if arr[i] != 'N':
            curr.left = Node(int(arr[i]))
            queue.append(curr.left)
        i += 1
        if i < len(arr) and arr[i] != 'N':
            curr.right = Node(int(arr[i]))
            queue.append(curr.right)
        i += 1
    return root

def right_view(root):
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.pop(0)
            if i == level_size - 1:
                result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return result

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = input().split()
        root = build_tree(arr)
        result = right_view(root)
        print(" ".join(map(str, result)))
