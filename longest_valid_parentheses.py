def push(stack, item):
    stack.append(item)
    return stack

def pop(stack):
    if stack:
        return stack.pop()
    return None

stack = []
valid = 0  

data = input()

for i in range(len(data)):
    if data[i] == '(':
        stack = push(stack, i) 
    
    elif data[i] == ')':
        if stack: 
            index = pop(stack) 
            if stack:
                valid = max(valid, i - stack[-1])  
            else:
                stack = push(stack, i)
print(valid)
