class Stack:
    def __init__(self):
        self.items = []
        self.top = -1
        
    def push(self, val):
        self.items.append(val)
        self.top += 1
    
    def pop(self):
        if self.top < 0:
            return False
            
        item = self.items.pop()
        self.top -= 1
        return item
        
    def peek(self):
        if self.top < 0:
            return False
        return self.items[self.top]
        
if __name__ == "__main__":
    queries = int(input())
    
    stack1 = Stack()
    stack2 = Stack()
    
    popped = []
    
    for i in range(queries):
        query = [int(i) for i in input().split()]
        
        if len(query) > 1: 
            stack1.push(query[1])
            
        else: 
            if stack2.top < 0:
                while stack1.top >= 0:
                    item = stack1.pop()
                    if item is not False:
                        stack2.push(item)
        
            popped_item = stack2.pop()
            if popped_item is not False:
                popped.append(str(popped_item))
            else:
                popped.append("-1")
            
    print(" ".join(popped))
