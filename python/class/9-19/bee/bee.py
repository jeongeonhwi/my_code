import sys
sys.stdin = open('input.txt', 'r')


def dfs(start, end, one, two):
    global max_v
    if start == end:
        max_v = max(max_v, one+two)
        return
    else:
        for i in range(N):
            for j in range(N-M+1):
                if used[i][j] == 0:
                    tmp = []
                    tmp_v = 0
                    for m in range(M):
                        used[i][j+m] = 1
                        tmp.append(arr[i][j+m])
                        tmp_v += arr[i][j+m]**2
                    if one < two:
                        new_one = tmp_v
                        new_two = two
                    else:
                        new_one = one
                        new_two = tmp_v
                    dfs(start+1, end, new_one, new_two)
                    for m in range(M):
                        used[i][j+m] = 0


T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [[0]*(N-M) for _ in range(N)]
    max_v = 0
    dfs(0, (N-M+1)*N, 0, 0)
    print(f'#{tc} {max_v}')