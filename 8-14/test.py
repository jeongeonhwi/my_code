#계산기2
'''
6528-*2/+
'''

stack = [0]*100
top = -1
s = str(input())
for x in s:
    # 피연산자면...
    if x not in '+-/*':
        # push(x)
        top += 1
        stack[top] = int(x)
    else:
        # pop()
        op2 = stack[top]
        top -= 1
        # pop()
        op1 = stack[top]
        top -= 1
        if x == '+':    # op1 + op2
            top += 1
            stack[top] = op1 + op2
        elif x == '-':
            top += 1
            stack[top] = op1 - op2
        elif x == '/':
            top += 1
            stack[top] = op1 / op2
        elif x == '*':
            top += 1
            stack[top] = op1 * op2
print(stack[0])