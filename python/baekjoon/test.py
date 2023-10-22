import sys
input = sys.stdin.readline






K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

start = 1
end = max(arr)
while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in arr:
        cnt+= i//mid

    if cnt < N:
        end = mid-1

    if cnt >= N:
        start = mid+1

print(end)