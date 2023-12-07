import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque
N,K = map(int, input().split())
pus = [i for i in range(1,N+1)]
pus = deque(pus)
now = 1
result = []
while pus:
    tmp = pus.popleft()
    if now==K:
        result.append(tmp)
        now = 1
        continue
    now +=1
    pus.append(tmp)
print('<', end='')
for i in range(len(result)):
    if i == len(result)-1:
        print(result[i], end='')
        continue
    print(f'{result[i]}, ', end='')
print('>')