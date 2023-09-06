import sys
sys.stdin = open('input.txt', 'r')

def game(i, K, time):
    global min_v
    if time > min_v:
        return
    if i == K:
        min_v = min(min_v, time)
        return
    if i > K:
        min_v = min(min_v, time+i-K)
        return
    else:
        game(i*2, K, time+1)
        game(i*2-1, K, time+1+1)
        game(i+1, K, time+1)


N, K = map(int, input().split())
check = True
if N == K:
    print(0)
    check = False
elif N>K:
    print(N-K)
    check = False
if check:
    visited = [0]*K*2
    min_v = K-N
    game(N, K, 0)
    print(min_v)


