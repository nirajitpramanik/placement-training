def precedence(operator1, operator2):
    ops = {
        3: ["^"],
        2: ["*", "/"],
        1: ["+", "-"]
    }

    o1, o2 = 0, 0
    for prec in ops:
        if operator1 in ops[prec]:
            o1 = prec
        if operator2 in ops[prec]:
            o2 = prec

    if operator1 == "^" and operator2 == "^":
        return 2 if o1 > o2 else 1

    if o1 > o2:
        return 2
    elif o1 == o2:
        return 1
    else:
        return 0


def is_operator(char):
    return char in "+-*/^"


postfix = ""
stack = []

infix = input()

for var in infix:
    if var.isalnum(): 
        postfix += var
    elif var == '(':
        stack.append(var)
    elif var == ')':
        while stack and stack[-1] != '(':
            postfix += stack.pop()
        if stack and stack[-1] == '(':
            stack.pop()
    elif is_operator(var):
        while (stack and stack[-1] != '(' and
               precedence(var, stack[-1]) <= 1): 
            postfix += stack.pop()
        stack.append(var)

while stack:
    postfix += stack.pop()

print(postfix)
