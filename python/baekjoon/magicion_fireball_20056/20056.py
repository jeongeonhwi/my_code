import sys
sys.stdin = open('input.txt', 'r')

# 파이어볼 정보 i, j, m, 속력, 방향 인덱스들은 마이너스1해줘야함
N, M, K = map(int, input().split())
arr = [[0]*N for _ in range(N)]
for _ in range(M):
    i, j, m, s, d = map(int, input().split())
    arr[i-1][j-1] = [[i-1,j-1,m,s,d]]
direction = [[-1, 0], [-1, 1], [0, 1], [1,1], [1, 0], [1,-1], [0,-1], [-1, -1]]
all_d = [0,2,4,6]
else_d = [1,3,5,7]
for k in range(K):
    visited=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and visited[i][j] == 0:
                if len(arr[i][j]) == 1:
                    arr[i][j][0][0] = (arr[i][j][0][0]+direction[arr[i][j][0][4]][0]*arr[i][j][0][3])%N
                    arr[i][j][0][1] = (arr[i][j][0][1]+direction[arr[i][j][0][4]][1]*arr[i][j][0][3])%N
                    if arr[arr[i][j][0][0]][arr[i][j][0][1]] == 0:
                        arr[arr[i][j][0][0]][arr[i][j][0][1]] = [arr[i][j][0]]
                        visited[arr[i][j][0][0]][arr[i][j][0][1]] = 1
                    else:
                        arr[arr[i][j][0][0]][arr[i][j][0][1]].append(arr[i][j][0])
                        visited[arr[i][j][0][0]][arr[i][j][0][1]] = 1
                    arr[i][j] = 0
                else:
                    for ii in range(4):
                        arr[i][j][ii][0] = (arr[i][j][ii][0] + direction[arr[i][j][ii][4]][0] * arr[i][j][ii][3]) % N
                        arr[i][j][ii][1] = (arr[i][j][ii][1] + direction[arr[i][j][ii][4]][1] * arr[i][j][ii][3]) % N
                        if arr[arr[i][j][ii][0]][arr[i][j][ii][1]] == 0:
                            arr[arr[i][j][ii][0]][arr[i][j][ii][1]] = [arr[i][j][ii]]
                            visited[arr[i][j][ii][0]][arr[i][j][ii][1]] = 1
                        else:
                            arr[arr[i][j][ii][0]][arr[i][j][ii][1]].append(arr[i][j][ii])
                            visited[arr[i][j][ii][0]][arr[i][j][ii][1]] = 1
                    arr[i][j] = 0
    for i in range(N):
        for j in range(N):
            if type(arr[i][j]) == list and len(arr[i][j]) > 1:
                even = 0
                old = 0
                total_m = 0
                total_s = 0
                for ii in range(len(arr[i][j])):
                    total_m += arr[i][j][ii][2]
                    total_s += arr[i][j][ii][3]
                    if arr[i][j][ii][4]%2 == 1:
                        old += 1
                    else:
                        even += 1
                total_m = total_m//5
                total_s = total_s//len(arr[i][j])
                if total_m == 0:
                    arr[i][j] = 0
                    continue
                else:
                    arr[i][j] = []
                if len(arr[i][j]) == old or len(arr[i][j]) == even:
                    for dd in all_d:
                        arr[i][j].append([i,j,total_m,total_s,dd])
                else:
                    for dd in else_d:
                        arr[i][j].append([i, j, total_m, total_s, dd])
ans = 0
# for a in arr:
#     print(a)
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            for ii in arr[i][j]:
                ans += ii[2]
print(ans)