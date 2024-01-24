import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def dfs(s):
    visited = [0]*(N+2)
    visited[0] = 1
    stack = [s]
    while stack:
        i,j = arr[stack.pop()]
        for n in range(N+2):
            ni,nj = arr[n][0], arr[n][1]
            if visited[n] == 0:
                if abs(i-ni)+abs(j-nj) <= 1000:
                    stack.append(n)
                    visited[n] = 1
                    if ni == end[0] and nj == end[1]:
                        print('happy')
                        return
    print('sad')
    return



T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N+2)]
    start = (0,0)
    end = tuple(arr[-1])
    dfs(0)
