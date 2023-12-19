import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N, K = map(int, input().split())
arr = []
for _ in range(N):
    data = int(input())
    if data > K:
        continue
    arr.append(data)
arr.reverse()
coin = 0
for i in arr:
    if K >= i:
        coin += K//i
        K %= i
print(coin)