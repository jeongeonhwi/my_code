'''
문제 접근 : 처음에는 해당하는 감시카메라들을 스텍에 넣고 방향을 돌려서 이차원 리스트에
뿌릴까 했지만 예외 상황이 무조건 있을거 같아서 중복순열로 접근하기로 결정
방향들을 0부터 3까지의 숫자로 설정하고 카메라의 숫자만큼 중복순열 생성하여 품
사용한 함수는 2개로 카메라 위치를 찾아 스텍에 넣는 find_camera, 중복순열 함수인
permutation.

연산을 줄이기 위한 노력
1. 5번은 어차피 방향에 상관 없기 때문에 제외함.
'''



import sys
sys.stdin = open('input.txt', 'r')
import copy

def find_camera(arr):
    stack = []
    stack5 = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and arr[i][j] != 6 and arr[i][j] != 5:
                stack.append((i, j))
            elif arr[i][j] == 5:
                stack5.append((i, j))
    return stack, stack5


def permutation(i, N, K):
    if i == K:
        c = p[:]
        perlist.append(c)
        return
    else:
        for j in range(N):
            p[i] = dirt1[j]
            permutation(i+1, N, K)




#    위 오른쪽 아래 왼쪽
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

N, M = map(int, input().split())
arr2 = [list(map(int, input().split())) for _ in range(N)]
arr = copy.deepcopy(arr2)
stack, stack5 = find_camera(arr)
perlist = []
dirt1 = [0, 1, 2, 3]
p = [0]*len(stack)
K = len(stack)
permutation(0, 4, K)
min_v = N*M
for per in perlist:
    tmpcount = 0
    tmpstack = stack[:]
    tmpstack5 = stack5[:]
    for k in per:
        i, j = tmpstack.pop()
        if arr[i][j] == 1:
            ni = i +di[k]
            nj = j +dj[k]
            while True:
                if 0<=ni<N and 0<=nj<M:
                    if arr[ni][nj] != 6:
                        if arr[ni][nj] == 0:
                            arr[ni][nj] = -1
                            ni += di[k]
                            nj += dj[k]
                        else:
                            ni += di[k]
                            nj += dj[k]
                    else:
                        break
                else:
                    break
        elif arr[i][j] == 2:
            ni = i +di[k]
            nj = j +dj[k]
            nni = i-di[k]
            nnj = j-dj[k]
            while True:
                if 0<=ni<N and 0<=nj<M:
                    if arr[ni][nj] != 6:
                        if arr[ni][nj] == 0:
                            arr[ni][nj] = -1
                            ni += di[k]
                            nj += dj[k]
                        else:
                            ni += di[k]
                            nj += dj[k]
                    else:
                        break
                else:
                    break
            while True:
                if 0<=nni<N and 0<=nnj<M:
                    if arr[nni][nnj] != 6:
                        if arr[nni][nnj] == 0:
                            arr[nni][nnj] = -1
                            nni -= di[k]
                            nnj -= dj[k]
                        else:
                            nni -= di[k]
                            nnj -= dj[k]
                    else:
                        break
                else:
                    break
        elif arr[i][j] == 3:
            ni = i +di[k]
            nj = j +dj[k]
            nnni = i+di[(k+1)%4]
            nnnj = j+dj[(k+1)%4]
            while True:
                if 0<=ni<N and 0<=nj<M:
                    if arr[ni][nj] != 6:
                        if arr[ni][nj] == 0:
                            arr[ni][nj] = -1
                            ni += di[k]
                            nj += dj[k]
                        else:
                            ni += di[k]
                            nj += dj[k]
                    else:
                        break
                else:
                    break
            while True:
                if 0<=nnni<N and 0<=nnnj<M:
                    if arr[nnni][nnnj] != 6:
                        if arr[nnni][nnnj] == 0:
                            arr[nnni][nnnj] = -1
                            nnni += di[(k+1)%4]
                            nnnj += dj[(k+1)%4]
                        else:
                            nnni += di[(k+1)%4]
                            nnnj += dj[(k+1)%4]
                    else:
                        break
                else:
                    break
        elif arr[i][j] == 4:
            ni = i +di[k]
            nj = j +dj[k]
            nni = i-di[k]
            nnj = j-dj[k]
            nnni = i+di[(k+1)%4]
            nnnj = j+dj[(k+1)%4]
            while True:
                if 0<=ni<N and 0<=nj<M:
                    if arr[ni][nj] != 6:
                        if arr[ni][nj] == 0:
                            arr[ni][nj] = -1
                            ni += di[k]
                            nj += dj[k]
                        else:
                            ni += di[k]
                            nj += dj[k]
                    else:
                        break
                else:
                    break
            while True:
                if 0<=nni<N and 0<=nnj<M:
                    if arr[nni][nnj] != 6:
                        if arr[nni][nnj] == 0:
                            arr[nni][nnj] = -1
                            nni -= di[k]
                            nnj -= dj[k]
                        else:
                            nni -= di[k]
                            nnj -= dj[k]
                    else:
                        break
                else:
                    break
            while True:
                if 0<=nnni<N and 0<=nnnj<M:
                    if arr[nnni][nnnj] != 6:
                        if arr[nnni][nnnj] == 0:
                            arr[nnni][nnnj] = -1
                            nnni += di[(k+1)%4]
                            nnnj += dj[(k+1)%4]
                        else:
                            nnni += di[(k+1)%4]
                            nnnj += dj[(k+1)%4]
                    else:
                        break
                else:
                    break
    while tmpstack5:
        i, j = tmpstack5.pop()
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            while True:
                if 0<=ni<N and 0<=nj<M:
                    if arr[ni][nj] != 6:
                        if arr[ni][nj] == 0:
                            arr[ni][nj] = -1
                            ni += di[k]
                            nj += dj[k]
                        else:
                            ni += di[k]
                            nj += dj[k]
                    else:
                        break
                else:
                    break
    for n in range(N):
        tmpcount += arr[n].count(0)
    if tmpcount < min_v:
        min_v = tmpcount
    # for kkk in range(N):
    #     print(arr[kkk])
    arr = copy.deepcopy(arr2)
print(min_v)