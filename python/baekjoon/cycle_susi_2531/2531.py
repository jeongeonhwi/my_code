import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 접시수, 초밥수, 연속수, 쿠폰번호
N, D, K, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
max_v = 0
for i in range(N):
    susi = set()
    for k in range(K):
        susi.add(arr[(i+k)%N])
    susi.add(C)
    max_v = max(max_v, len(susi))
print(max_v)