class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, val):
        self.items.append(val)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[-1] if self.items else None
        
def is_operator(var):
    return var in "+-*/()"
    
def precedence(op1, op2):
    prec = {
        2: ["*", "/"],
        1: ["+", "-"]
    }
    
    lvl1, lvl2 = 0, 0
    
    for level in prec:
        if op1 in prec[level]:
            lvl1 = level
        if op2 in prec[level]:
            lvl2 = level
            
    return lvl1 <= lvl2
    
def perform_operation(operator, operand1, operand2):
    if operator == "+":
        return operand2 + operand1
        
    elif operator == "-":
        return operand2 - operand1
    
    elif operator == "*":
        return operand2 * operand1
        
    elif operator == "/":
        return operand2 // operand1
        
if __name__ == "__main__":
    operand_stack = Stack()
    operator_stack = Stack()
    
    expression = [i for i in input().split()]
    
    for var in expression:
        if not is_operator(var):
            operand_stack.push(int(var))
        else:
            while operator_stack.peek() and precedence(var, operator_stack.peek()):
                opn = operator_stack.pop()
                opd1 = operand_stack.pop()
                opd2 = operand_stack.pop()
                operand_stack.push(perform_operation(opn, opd1, opd2))
                
            operator_stack.push(var)
    
    while operator_stack.peek():
        opn = operator_stack.pop()
        opd1 = operand_stack.pop()
        opd2 = operand_stack.pop()
        operand_stack.push(perform_operation(opn, opd1, opd2))
    
    print(operand_stack.peek())
