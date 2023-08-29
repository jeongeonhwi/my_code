import sys
sys.stdin = open('input.txt', 'r')



import copy
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]


N = int(input())
arr2 = [list(map(int, input().split())) for _ in range(N)]
arr = copy.deepcopy(arr2)
for i1 in range(4):
    for i2 in range(4):
        for i3 in range(4):
            for i4 in range(4):
                for i5 in range(4):
                    direct = [0]*10
                    direct[0] = di[i1]
                    direct[1] = dj[i1]
                    direct[2] = di[i2]
                    direct[3] = dj[i2]
                    direct[4] = di[i3]
                    direct[5] = dj[i3]
                    direct[6] = di[i4]
                    direct[7] = dj[i4]
                    direct[8] = di[i5]
                    direct[9] = dj[i5]
                    for k in range(5):
                        for i in range(N):
                            for j in range(N):
                                ni = i+direct[k*2]
                                nj = j+direct[k*2+1]
                                if arr[i][j] != 0:
                                    if 0<=ni<N and 0<=nj<N:
                                        while True:
                                            if arr[i][j] == arr[ni][nj]:
                                                arr[i][j] = 0
                                                arr[ni][nj] += arr[ni][nj]
                                                break
                                            elif arr[ni][nj] == 0:
                                                ni += direct[k*2]
                                                nj += direct[k*2+1]
                                            else:
                                                break

