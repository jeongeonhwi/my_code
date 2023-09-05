import sys
sys.stdin = open('input.txt', 'r')

isp = {')':3, '*':2, '+':1, '-':1, '(':0}
N = int(input())
stack = []
s = []
a_str = input()
check = False
checkplus = False
for i in range(len(a_str)):
    if i%2==0:
        stack.append(int(a_str[i]))
    else:
        if s:
            if a_str[i] == '*' and s[-1] == '+':
                tmp = s.pop()
                s.append('(')
                s.append(tmp)
                s.append(')')
                s.append(a_str[i])
            elif a_str[i] == '+' and s[-1] == '*':
                s.append('(')
                s.append(a_str[i])
                s.append(')')
            elif a_str[i] == '-' and s[-1] == '-':
                s.append('(')
                s.append(a_str[i])
                s.append(')')
            else:
                s.append(a_str[i])
        else:      
            s.append(a_str[i])
print(s)
print(stack)
susik = []
idx = 0
while s:
    tmp = s.pop(0)
    if tmp != '(':
        if susik:
            if susik[-1] != ')':
                susik.append(tmp)
                susik.append(stack.pop(0))
            else:
                susik.append(tmp)
                susik.append(stack.pop(0))
        else:
            susik.append(stack.pop(0))
            susik.append(tmp)
            susik.append(stack.pop(0))
    else:
        a = stack.pop(0)
        susik.append(tmp)
        susik.append(a)
        tmp = s.pop(0)
        susik.append(tmp)
        susik.append(stack.pop(0))
        tmp = s.pop(0)
        susik.append(tmp)
print(susik)
s = []
stack = []
for i in susik:
    if type(i) == int:
        stack.append(i)
    else:
        if i == ')':
            a = stack.pop()
            b = stack.pop()
            s1 = s.pop()
            if s1 == '+':
                s2 = a+b
            elif s1 == '-':
                s2 = a-b
            else:
                s2 = a*b
            stack.append(s2)
            s.pop()
        else:
            s.append(i)

result = 0
while s:
    s1 = stack.pop(0)
    s2 = stack.pop(0)
    s3 = s.pop(0)
    tmp = 0
    if s3 == '+':
        tmp = s1+s2
    elif s3 == '-':
        tmp = s1-s2
    else:
        tmp = s1*s2
    stack.insert(0, tmp)
result = stack[0]
print(result)