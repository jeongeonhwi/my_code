N = int(input())
arr2 = [list(map(int, input().split())) for _ in range(N)]
# 아래 위 오른쪽 왼쪽
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
direct = [0]*10
arr = []
for i in arr2:
    arr.append(i[:])
max_v = 0
for i1 in range(4):
    for i2 in range(4):
        for i3 in range(4):
            for i4 in range(4):
                for i5 in range(4):
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
                        if direct[k*2]==1 and direct[k*2+1]==0:
                            for j in range(N):
                                i = 0
                                stack = []
                                if arr[i][j] != 0:
                                    stack.append(arr[i][j])
                                    arr[i][j] = 0
                                ni = i+direct[k*2]
                                nj = j+direct[k*2+1]
                                while True:
                                    if 0<=ni<N and 0<=nj<N:
                                        if arr[ni][nj] != 0:
                                            stack.append(arr[ni][nj])
                                            arr[ni][nj] = 0
                                            ni += direct[k*2]
                                            nj += direct[k*2+1]
                                        else:
                                            ni += direct[k*2]
                                            nj += direct[k * 2 + 1]
                                    else:
                                        break
                                stack.reverse()
                                for ss in range(len(stack)-1):
                                    if ss == 0:
                                        if stack[ss] == stack[ss+1]:
                                            stack[ss] = 0
                                            stack[ss+1] *= 2
                                    else:
                                        if stack[ss-1] != 0 and stack[ss] == stack[ss+1]:
                                            stack[ss] = 0
                                            stack[ss+1] *= 2
                                stack.reverse()
                                stack2 = []
                                for sss in stack:
                                    if sss != 0:
                                        stack2.append(sss)
                                for s in range(1, len(stack2)+1):
                                    arr[N-s][j] = stack2.pop()


                        elif direct[k*2]==-1 and direct[k*2+1]==0:
                            for j in range(N):
                                i = N-1
                                stack = []
                                if arr[i][j] != 0:
                                    stack.append(arr[i][j])
                                    arr[i][j] = 0
                                ni = i+direct[k*2]
                                nj = j+direct[k*2+1]
                                while True:
                                    if 0<=ni<N and 0<=nj<N:
                                        if arr[ni][nj] != 0:
                                            stack.append(arr[ni][nj])
                                            arr[ni][nj] = 0
                                            ni += direct[k*2]
                                            nj += direct[k*2+1]
                                        else:
                                            ni += direct[k*2]
                                            nj += direct[k * 2 + 1]
                                    else:
                                        break
                                stack.reverse()
                                for ss in range(len(stack)-1):
                                    if ss == 0:
                                        if stack[ss] == stack[ss+1]:
                                            stack[ss] = 0
                                            stack[ss+1] *= 2
                                    else:
                                        if stack[ss-1] != 0 and stack[ss] == stack[ss+1]:
                                            stack[ss] = 0
                                            stack[ss+1] *= 2
                                stack.reverse()
                                stack2 = []
                                for sss in stack:
                                    if sss != 0:
                                        stack2.append(sss)
                                for s in range(len(stack2)):
                                    arr[s][j] = stack2.pop()


                        elif direct[k*2]==0 and direct[k*2+1]==1:
                            for i in range(N):
                                j = 0
                                stack = []
                                if arr[i][j] != 0:
                                    stack.append(arr[i][j])
                                    arr[i][j] = 0
                                ni = i+direct[k*2]
                                nj = j+direct[k*2+1]
                                while True:
                                    if 0<=ni<N and 0<=nj<N:
                                        if arr[ni][nj] != 0:
                                            stack.append(arr[ni][nj])
                                            arr[ni][nj] = 0
                                            ni += direct[k*2]
                                            nj += direct[k*2+1]
                                        else:
                                            ni += direct[k*2]
                                            nj += direct[k * 2 + 1]
                                    else:
                                        break
                                stack.reverse()
                                for ss in range(len(stack)-1):
                                    if ss == 0:
                                        if stack[ss] == stack[ss+1]:
                                            stack[ss] = 0
                                            stack[ss+1] *= 2
                                    else:
                                        if stack[ss-1] != 0 and stack[ss] == stack[ss+1]:
                                            stack[ss] = 0
                                            stack[ss+1] *= 2
                                stack.reverse()
                                stack2 = []
                                for sss in stack:
                                    if sss != 0:
                                        stack2.append(sss)
                                for s in range(1, len(stack2)+1):
                                    arr[i][N-s] = stack2.pop()


                        elif direct[k*2]==0 and direct[k*2+1]==-1:
                            for i in range(N):
                                j = N-1
                                stack = []
                                if arr[i][j] != 0:
                                    stack.append(arr[i][j])
                                    arr[i][j] = 0
                                ni = i+direct[k*2]
                                nj = j+direct[k*2+1]
                                while True:
                                    if 0<=ni<N and 0<=nj<N:
                                        if arr[ni][nj] != 0:
                                            stack.append(arr[ni][nj])
                                            arr[ni][nj] = 0
                                            ni += direct[k*2]
                                            nj += direct[k*2+1]
                                        else:
                                            ni += direct[k*2]
                                            nj += direct[k * 2 + 1]
                                    else:
                                        break
                                stack.reverse()
                                for ss in range(len(stack)-1):
                                    if ss == 0:
                                        if stack[ss] == stack[ss+1]:
                                            stack[ss] = 0
                                            stack[ss+1] *= 2
                                    else:
                                        if stack[ss-1] != 0 and stack[ss] == stack[ss+1]:
                                            stack[ss] = 0
                                            stack[ss+1] *= 2
                                stack.reverse()
                                stack2 = []
                                for sss in stack:
                                    if sss != 0:
                                        stack2.append(sss)
                                for s in range(len(stack2)):
                                    arr[i][s] = stack2.pop()
                    # print(arr)
                    tem_max = max(map(max, arr))
                    arr.clear()
                    for i in arr2:
                        arr.append(i[:])
                    if tem_max > max_v:
                        max_v = tem_max
print(max_v)



