import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort()
    top = 0
    ans = 1
    for i in range(1,N):
        if arr[i][1] < arr[top][1]:
            ans += 1
            top = i
    print(ans)