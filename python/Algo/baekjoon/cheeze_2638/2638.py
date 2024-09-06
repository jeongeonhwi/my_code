import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def check_out(si,sj):
    visited = [[0]*M for _ in range(N)]
    stack = [(si,sj)]
    visited[si][sj] = 1
    arr[si][sj] = 2
    while stack:
        i,j = stack.pop()
        for ni,nj in [(i+1,j),(i,j+1),(i-1,j),(i,j-1),]:
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0 and arr[ni][nj] != 1:
                visited[ni][nj] = 1
                arr[ni][nj] = 2
                stack.append((ni,nj))


def check_air(i,j):
    c = 0
    for ni,nj in [(i+1,j),(i,j+1),(i-1,j),(i,j-1),]:
        if arr[ni][nj] == 2:
            c+=1
    if c > 1:
        return True
    return False



N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
check_out(0,0)
hour = 0
cheeze_set = set()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cheeze_set.add((i, j))
while cheeze_set:
    hour += 1
    tmp = set()
    ok =set()
    for ci,cj in cheeze_set:
        if check_air(ci,cj):
            ok.add((ci,cj))
        else:
            tmp.add((ci,cj))
    cheeze_set = tmp
    for oi,oj in ok:
        arr[oi][oj] = 2
    check_out(0,0)
print(hour)