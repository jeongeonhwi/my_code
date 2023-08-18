import sys
sys.stdin =open('input.txt')

isp = {'+':1, '-':1, '/':2, '*':2}
T = int(input())
fx = str(input())
s = ''
stack = []
for i in fx:
    if i not in '+-/*':
        s += i
    else:
        if len(stack) ==0 or isp[stack[-1]] <= isp[i]:
            stack.append(i)
        elif isp[stack[-1]] > isp[i]:
            while len(stack) > 0 and isp[stack[-1]] > isp[i]:
                s += stack.pop()
            stack.append(i)
for _ in range(len(stack)):
    s += stack.pop()
print(f'#{T} {s}')