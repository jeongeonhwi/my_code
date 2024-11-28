import sys
sys.stdin = open('input.txt','r')

arr = input()
stack = []
s = ""
b = []
for a in arr:
    if a == '-':
        b.append('-')
        s+=' '
    elif a == '+':
        b.append('+')
        s+=' '
    else:
        s+=a
stack = list(map(int, s.split()))
tmp = [stack.pop(0)]
while stack:
    tmp.append(b.pop(0))
    tmp.append(stack.pop(0))
stack = tmp[:]
tmp = []
while stack:
    i = stack.pop(0)
    if i == '+':
        ii = stack.pop(0)
        ii += tmp.pop()
        tmp.append(ii)
    else:
        tmp.append(i)
stack = tmp[:]
tmp = []
while stack:
    i = stack.pop(0)
    if i == '-':
        ii = stack.pop(0)
        ii = tmp.pop() - ii
        tmp.append(ii)
    else:
        tmp.append(i)
print(tmp[0])