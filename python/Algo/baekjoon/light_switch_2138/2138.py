import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


N = int(input())
before = list(input())
after = list(input())
before2 = before[:]
ans = 0
ans2 = 0

# 처음 스위치를 켜지 않음
for i in range(1, N):
    if before[i-1] != after[i-1]:
        ans += 1
        for j in range(i-1, i+2):
            if j < N:
                if before[j] == '0':
                    before[j] = '1'
                else:
                    before[j] = '0'

# 처음 스위치를 켬
if before2[0] == '0':
    before2[0] = '1'
else:
    before2[0] = '0'

if before2[1] == '0':
    before2[1] = '1'
else:
    before2[1] = '0'

ans2 += 1
for i in range(1, N):
    if before2[i-1] != after[i-1]:
        ans2 += 1
        for j in range(i-1, i+2):
            if j < N:
                if before2[j] == '0':
                    before2[j] = '1'
                else:
                    before2[j] = '0'

for i in range(N):
    if before[i] != after[i]:
        ans = float('inf')
    if before2[i] != after[i]:
        ans2 = float('inf')
if ans == ans2 == float('inf'):
    print(-1)
else:
    print(min(ans,ans2))