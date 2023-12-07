import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 버전1이 메모리초과 나서 add 대신 함수 내부에서 실행하니까 시간초과남
def permutation(start, end):
    global min_v
    if start == end:
        start = 0
        link = 0
        for i in range(N // 2):
            for j in range(N // 2):
                start += arr[m[i]][m[j]]
                link += arr[m[N // 2 + i]][m[N // 2 + j]]
        min_v = min(min_v, abs(start - link))
        return
    for j in range(N):
        if used[j] == 0:
            m[start] = num[j]
            used[j] = 1
            permutation(start+1, end)
            used[j] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
num = [i for i in range(N)]
used = [0]*N
m = [0]*N
my_set = set()
min_v = 10000
permutation(0,N)

print(min_v)