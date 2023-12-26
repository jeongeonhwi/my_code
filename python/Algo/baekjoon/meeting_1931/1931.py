import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    s,e = map(int, input().split())
    arr.append((s,e))
arr.sort(key=lambda  x: (x[1], x[0]))
cnt = 0
end = -1
for i in arr:
    if i[0] >= end:
        cnt +=1
        end = i[1]
print(cnt)