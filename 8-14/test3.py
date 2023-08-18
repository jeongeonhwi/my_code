'''
(6+5*(2-8)/2)
'''

icp = {'(':3, '+':1, '-':1, '/':2, '*':2}
isp = {'(':0, '+':1, '-':1, '/':2, '*':2}
stack = [0]*1000
top = -1
arr = str(input())
s = ''
for i in arr:
    if i not in '(*/+-)':
        s += i
    elif i == ')':
        while stack[top] != '(':
            s += stack[top]
            top -= 1
        top -= 1
    else:
        if top == -1 or isp[stack[top]] <= icp[i]:
            top += 1
            stack[top] = i
print(s)

stack = [0]*100
