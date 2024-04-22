import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N,L,R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

save = []
ans = 0
while True:
    for i in range(N):
        for j in range(N):
            for ni, nj in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                if 0<=ni<N and 0<=nj<N:
                    if L<= abs(arr[i][j] - arr[ni][nj]) <= R:
                        save.add((ni,nj))
                        save.add((i,j))
    if len(save) == 0:
        break
    ans += 1
    sumdata = 0
    for si,sj in save:
        sumdata += arr[si][sj]
    chageData = sumdata // len(save)
    for si,sj in save:
        arr[si][sj] = chageData
    save.clear()

print(ans)