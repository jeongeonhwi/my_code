import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

# 음수는 이미 설치된 고석철도
# 10000을 넘지 않는 지연수는 설치 비용


from heapq import heappop, heappush

def daic(s):
    visited = [(float('inf'),1,1)]*(N)
    hq = [(0,s,-1)]
    visited[s] = (0,s,-1)
    while hq:
        cnt,i, pi = heappop(hq)
        print(i,hq)
        if visited[i][0] < cnt:
            continue
        for ni in range(N):
            next_cnt = cnt + arr[i][ni]
            if visited[ni][0] <= next_cnt:
                continue
            visited[ni] = (next_cnt,pi,i)
            heappush(hq, (next_cnt,ni, i))
            print(next_cnt,ni,i)
    return visited


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cost = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] < 0:
            cost += arr[i][j]
            arr[i][j] = 0
cost //= 2

print(daic(0))