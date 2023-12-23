import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N,M = map(int, input().split())
arr = dict()
for _ in range(N):
    site, password = input().strip().split()
    arr[site] = password
for _ in range(M):
    site = input().strip()
    print(arr[site])