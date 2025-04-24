import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
K = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(K):
    a,b = map(int, input().split())
    arr[a-1][b-1] = 2
