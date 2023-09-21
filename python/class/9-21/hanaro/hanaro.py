import sys
sys.stdin = open('input.txt', 'r')



import heapq

def dijkstra(start):
    MST = [[int(1e15)]*1000005 for _ in range(1000005)]
    pq = []
    heapq.heappush(pq, (start))
    MST[x_idx[0]][y_idx[0]] = 0
    while pq:
        money, x, y = heapq.heappop(pq)
        if MST[x][y] < money:
            continue
        for j,i in my_set:
            if x != j and y != i:
                next_money = E*((x_idx[j]-x_idx[x])**2+(y_idx[i]-y_idx[y])**2)
                if MST[i] <= next_money:
                    continue
                MST[i] = next_money
                heapq.heappush(pq, (next_money, i))
    return MST


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_idx = list(map(int, input().split()))
    y_idx = list(map(int, input().split()))
    E = float(input())
    my_set = set()
    for i in range(1, N):
        my_set.add((x_idx[i], y_idx[i]))
    ans = dijkstra((0, x_idx[0], y_idx[0]))
    print(f'#{tc} {ans}')