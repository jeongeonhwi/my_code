import sys
input = sys.stdin.readline


from heapq import heappop, heappush
n = int(input())
card = [int(input()) for _ in range(n)]
card.sort()
ans = 0
if len(card) > 1:
    while True:
        if len(card) == 2:
            ans += card[0]+card[1]
            break
        a,b = heappop(card), heappop(card)
        ans += (a+b)
        heappush(card, (a+b))
print(ans)