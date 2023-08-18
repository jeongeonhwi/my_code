import sys
sys.stdin = open('input.txt')

icp = {'+':1, '-':1, '/':2, '*':2, '(':3}
isp = {'+':1, '-':1, '/':2, '*':2, '(':0}

T = int(input())
for tc in range(1, T+1):
    arr = list(map(str,input().split()))
    arr.pop()
    stack = []
    try:
        for i in arr:
            if i not in '+-/*':
                stack.append(int(i))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if i == '+':
                    a = op1 + op2
                    stack.append(a)
                elif i == '-':
                    a = op1 - op2
                    stack.append(a)
                elif i == '/':
                    a = op1 // op2
                    stack.append(a)
                elif i == '*':
                    a = op1 * op2
                    stack.append(a)
    except:
        stack = ['error']
    if len(stack) > 1:
        stack = ['error']
    print(f'#{tc} {stack[0]}')