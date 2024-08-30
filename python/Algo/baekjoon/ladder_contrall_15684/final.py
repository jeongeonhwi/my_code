import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N,M,H = map(int, input().split())
arr = [[0]*N for _ in range(H)]
for _ in range(M):
    i,j = map(int, input().split())
    i,j = i-1,j-1
    arr[i][j] = 1
    arr[i][j+1] = -1

print(arr)
