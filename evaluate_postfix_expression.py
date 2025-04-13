def is_operator(var):
    return var in "+-*/^"

postfix = input()
stack = []
temp = ''

for var in postfix:
    if not is_operator(var) and var != ' ':
        temp += var
    elif var == ' ':
        if temp:
            stack.append(int(temp))
            temp = ''
    else:
        op1 = stack.pop()
        op2 = stack.pop()
        
        if var == "+":
            res = op2 + op1
        elif var == "-":
            res = op2 - op1
        elif var == "*":
            res = op2 * op1
        elif var == "/":
            res = op2 // op1
        else:
            res = op2 ** op1
            
        stack.append(res)

print(int(stack[-1]))
