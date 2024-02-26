import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs():
    pass


N,M,H = map(int, input().split())
raro = set()
for _ in range(M):
    data = map(int, input().split())
    raro.add(tuple(data))

min_v = float('inf')
cnt = 0

if 