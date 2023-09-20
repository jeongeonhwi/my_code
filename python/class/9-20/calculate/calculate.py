import sys
sys.stdin = open('input.txt', 'r')



# +1, -1, *2, -10 네 가지를 가지고 M을 만들자
# 각 각을 0부터 3이라는 수를 붙인다.

from collections import deque


def bfs(start, end):
    visited = [0]*3000000
    visited[start] = 1
    q = [(start, 0)]
    min_v = 0
    q = deque(q)
    while q:
        i, cnt, = q.popleft()
        if i == end:
            min_v = cnt
            break
        else:
            tmp = i+1
            if visited[tmp] == 0 and 0<tmp<=1000000:
                visited[tmp] = 1
                q.append((tmp, cnt+1))
            tmp2 = i-1
            if visited[tmp2] == 0 and 0<tmp2<=1000000:
                visited[tmp2] = 1
                q.append((tmp2, cnt+1))
            tmp3 = i-10
            if visited[tmp3] == 0 and 0<tmp3<=1000000:
                visited[tmp3] = 1
                q.append((tmp3, cnt+1))
            tmp4 = i*2
            if visited[tmp4] == 0 and 0<tmp4<=1000000:
                visited[tmp4] = 1
                q.append((tmp4, cnt+1))
        # print(i, cnt)
    return min_v


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    min_v = bfs(N, M)
    print(f'#{tc} {min_v}')