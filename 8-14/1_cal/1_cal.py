import sys
sys.stdin = open('input.txt')

isp = {'+':1}

T = 10
for tc in range(1, T+1):
    N = int(input())
    fx = str(input())
    s = ''
    stack = []
    for i in fx:
        if i not in '+':
            s += i
        elif i in '+':
            if len(stack) == 0 or isp[stack[-1]] <= isp[i]:
                stack.append(i)
            while len(stack) != 0 and isp[stack[-1]] > isp[i]:
                s += stack.pop()
    for _ in range(len(stack)):
        s += stack.pop()

    for i in s:
        if i not in '+':
            stack.append(i)
        elif i == '+':
            op2 = stack.pop()
            op1 = stack.pop()
            a = int(op1) + int(op2)
            stack.append(a)
    print(f'#{tc} {stack[0]}')
