import sys
input = sys.stdin.readline
# sys.stdin = open('input.txt', 'r')


N = int(input())
stack = []
for _ in range(N):
    data = input().strip()
    if data[:2] == 'pu':
        order, number = data.split()
        stack.append(number)
        continue
    if data == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
        continue
    if data == 'size':
        print(len(stack))
        continue
    if data == 'empty':
        if stack:
            print(0)
        else:
            print(1)
        continue
    if data == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
        continue