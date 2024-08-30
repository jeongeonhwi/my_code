import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def dfs(si):
    memory_arr = [si]
    stack = [si]
    visited[si] = label
    while stack:
        pass

def check_arr():
    pass


T = int(input())
for _ in range(T):
    N = int(input())
    arr =[0]+ list(map(int, input().split()))
    visited = [0]*(N+1)
    label = 1
    print(arr)