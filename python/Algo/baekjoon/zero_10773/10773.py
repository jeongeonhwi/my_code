import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    data = int(input())
    if data == 0:
        stack.pop()
    else:
        stack.append(data)
print(sum(stack))