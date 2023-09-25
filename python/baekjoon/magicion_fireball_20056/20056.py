import sys
sys.stdin = open('input.txt', 'r')

# 파이어볼 정보 i, j, m, 속력, 방향 인덱스들은 마이너스1해줘야함
N, M, K = map(int, input().split())
arr = [[0]*N for _ in range(N)]
for _ in range(M):
    i, j, m, s, d = map(int, input().split())
    if d%2 == 0:
        dd = 2
    else:
        dd = 1
    arr[i-1][j-1] = [i-1,j-1,m, s ,d, s, 1, dd]
direction = [[-1, 0], [-1, 1], [0, 1], [1,1], [1, 0], [1,-1], [0,-1], [-1, -1]]
all_d = [0,2,4,6]
else_d = [1,3,5,7]
for k in range(K):
    visited=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and visited[i][j] == 0:
                if len(arr[i][j]) != 4:
                    arr[i][j][0] = (arr[i][j][0]+direction[arr[i][j][4]][0]*arr[i][j][3])%N
                    arr[i][j][1] = (arr[i][j][1]+direction[arr[i][j][4]][1]*arr[i][j][3])%N
                    if arr[arr[i][j][0]][arr[i][j][1]] == 0:
                        arr[arr[i][j][0]][arr[i][j][1]] = arr[i][j]
                        visited[arr[i][j][0]][arr[i][j][1]] = 1
                    else:
                        arr[arr[i][j][0]][arr[i][j][1]][2] += arr[i][j][2]
                        arr[arr[i][j][0]][arr[i][j][1]][5] += arr[i][j][3]
                        arr[arr[i][j][0]][arr[i][j][1]][6] += 1
                        visited[arr[i][j][0]][arr[i][j][1]] = 1
                    arr[i][j] = 0
                else:
                    for ii in range(4):
                        arr[i][j][ii][0] = (arr[i][j][ii][0] + direction[arr[i][j][ii][4]][0] * arr[i][j][ii][3]) % N
                        arr[i][j][ii][1] = (arr[i][j][ii][1] + direction[arr[i][j][ii][4]][1] * arr[i][j][ii][3]) % N
                        if arr[arr[i][j][ii][0]][arr[i][j][ii][1]] == 0:
                            arr[arr[i][j][ii][0]][arr[i][j][ii][1]] = arr[i][j][ii]
                            visited[arr[i][j][ii][0]][arr[i][j][ii][1]] = 1
                        else:
                            arr[arr[i][j][ii][0]][arr[i][j][ii][1]][2] += arr[i][j][ii][2]
                            arr[arr[i][j][ii][0]][arr[i][j][ii][1]][5] += arr[i][j][ii][3]
                            arr[arr[i][j][ii][0]][arr[i][j][ii][1]][6] += 1
                            if arr[arr[i][j][ii][0]][arr[i][j][ii][1]][7] == 1 and arr[i][j][ii][7]%2==0:
                                arr[arr[i][j][ii][0]][arr[i][j][ii][1]][7] = 0
                            elif arr[arr[i][j][ii][0]][arr[i][j][ii][1]][7] == 2 and arr[i][j][ii][7]%2==1:
                                arr[arr[i][j][ii][0]][arr[i][j][ii][1]][7] = 0
                            visited[arr[i][j][ii][0]][arr[i][j][ii][1]] = 1
                    arr[i][j] = 0
    for i in range(N):
        for j in range(N):
            tmp = []
            if type(arr[i][j]) == list and arr[i][j][6] > 1:
                if arr[i][j][2]//5 > 0:
                    if arr[i][j][7] == 0:
                        for dd in else_d:
                            tmp.append([arr[i][j][0], arr[i][j][1], arr[i][j][2]//5, arr[i][j][5]//arr[i][j][5], dd, arr[i][j][5]//arr[i][j][5], 1, 1])
                    else:
                        for dd in all_d:
                            tmp.append([arr[i][j][0], arr[i][j][1], arr[i][j][2]//5, arr[i][j][5]//arr[i][j][5], dd, arr[i][j][5]//arr[i][j][5], 1, 2])
                    arr[i][j] = tmp
ans = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            if len(arr[i][j]) == 8:
                ans += arr[i][j][2]
            else:
                for ii in arr[i][j]:
                    ans += ii[2]
print(ans)