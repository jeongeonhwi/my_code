import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N, M = map(int, input().split())
no_heared = set()
ans = []
for _ in range(N):
    no_heared.add(input().strip())
for _ in range(M):
    data = input().strip()
    if data in no_heared:
        ans.append(data)
ans.sort()
print(len(ans))
for _ in ans:
    print(_)