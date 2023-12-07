import sys
sys.stdin = open('input.txt', 'r')

# 파이어볼 정보 i, j, m, 속력, 방향 인덱스들은 마이너스1해줘야함
N, M, K = map(int, input().split())
arr = [[[] for _ in range(N)] for _ in range(N)]
fireball = []
for _ in range(M):
    i, j, m, s, d = map(int, input().split())
    fireball.append([i-1, j-1, m,s,d])
direction = [[-1, 0], [-1, 1], [0, 1], [1,1], [1, 0], [1,-1], [0,-1], [-1, -1]]
all_d = [0,2,4,6]
else_d = [1,3,5,7]
for k in range(K):
    while fireball:
        fire = fireball.pop()
        fire[0] = (fire[0]+direction[fire[4]][0]*fire[3])%N
        fire[1] = (fire[1] + direction[fire[4]][1] * fire[3])%N
        arr[fire[0]][fire[1]].append(fire)
    for i in range(N):
        for j in range(N):
            if len(arr[i][j]) == 1:
                fireball.append(arr[i][j].pop())
            elif len(arr[i][j]) == 0:
                continue
            else:
                sum_m = 0
                sum_s = 0
                odd = 0
                even = 0
                for ii in arr[i][j]:
                    sum_m += ii[2]
                    sum_s += ii[3]
                    if ii[4]%2 == 0:
                        even += 1
                    else:
                        odd += 1
                sum_m = sum_m//5
                sum_s = sum_s//len(arr[i][j])
                if sum_m > 0:
                    if odd==0 or even == 0:
                        for jj in all_d:
                            fireball.append([i,j,sum_m,sum_s,jj])
                    else:
                        for jj in else_d:
                            fireball.append([i, j, sum_m, sum_s, jj])
                    arr[i][j].clear()
                else:
                    arr[i][j].clear()
ans = 0
for i in fireball:
    ans += i[2]
print(ans)