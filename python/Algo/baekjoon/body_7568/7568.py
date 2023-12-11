import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    kg, cm = map(int, input().split())
    arr.append((kg,cm))
for i in arr:
    cnt = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            cnt += 1
    print(cnt, end=' ')
print()