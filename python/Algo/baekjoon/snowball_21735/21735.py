import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def make_snowball(now, snowball, step):
    global max_v
    max_v = max(snowball, max_v)
    if step == M:
        return
    if now+1<N:
        make_snowball(now+1, snowball+arr[now+1], step+1)
    if now+2<N:
        make_snowball(now+2, (snowball//2)+arr[now+2], step+1)



N,M = map(int, input().split())
arr = list(map(int, input().split()))
max_v = 0
make_snowball(-1, 1, 0)
print(max_v)