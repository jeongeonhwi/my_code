import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

from heapq import heappop, heappush
T = int(input())
for _ in range(T):
    N = int(input())
    sq = []
    lq = []
    cd = dict()
    for _ in range(N):
        order, data = map(str, input().strip().split())
        c = int(data)
        if order == 'I':
            if c in cd:
                cd[c] += 1
            else:
                cd[c] = 1
                heappush(sq, int(data))
                heappush(lq, -int(data))
        else:
            if check == 0:
                continue
            if data == '1':
                check -= 1
                heappop(lq)
            else:
                check -= 1
                heappop(sq)
    if check == 0:
        print('EMPTY')
    else:
        print(-heappop(lq), heappop(sq))