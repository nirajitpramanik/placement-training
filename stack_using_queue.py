class Queue:
    def __init__(self):
        self.items = []
        self.size = len(self.items)
        
    def enqueue(self, val):
        self.items.append(val)
        
    def dequeue(self):
        item = self.items.pop(0)
        return item
        
if __name__ == "__main__":
    queries = int(input())
    queue = Queue()
    
    popped = []
    
    for q in range(queries):
        query = [int(i) for i in input().split()]
        
        if len(query) == 2:
            q2 = Queue()
            q2.enqueue(query[1])
            
            for item in queue.items:
                q2.enqueue(item)
                
            queue = q2
            
        else:
            try:
                popped.append(str(queue.dequeue()))
            except:
                popped.append("-1")
            
    print(" ".join(popped))
