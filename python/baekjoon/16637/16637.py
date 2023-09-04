import sys
sys.stdin = open('input.txt', 'r')

isp = {')':3, '*':2, '+':1, '-':1}

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
susik = []
idx = 0
while s:
    tmp = s.pop(0)
    if tmp != '(':
        if susik:
            if susik[-1] != ')':
                susik.append(stack.pop(0))
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
        a = susik.pop()
        susik.append(tmp)
        susik.append(a)
        tmp = s.pop(0)
        susik.append(tmp)
        susik.append(stack.pop(0))
        tmp = s.pop(0)
        susik.append(tmp)
s = []
stack = []
while susik:
    #여기까지
    pass