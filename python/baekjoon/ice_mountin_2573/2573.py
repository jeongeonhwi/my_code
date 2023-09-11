import sys
sys.stdin = open('input.txt', 'r')


import copy

def find_first():
    arr2 = copy.deepcopy(arr)
    stack = []
    for i in range(N):
        for j in range(M):
            if arr2[i][j] != 0:
                stack.append((i,j))
                arr2[i][j] = 0
                return stack
    return False


def find_second():
    arr2 = copy.deepcopy(arr)
    stack = find_first()
    if stack != False:
        while stack:
            i, j = stack.pop()
            arr2[i][j] = 0
            for k in range(4):
                ni = i+di[k]
                nj = j+dj[k]
                if 0<=ni<N and 0<=nj<M:
                    if arr2[ni][nj] != 0:
                        stack.append((i,j))
                        arr2[i][j] = 0
        for i in arr2:
            if i.count(0) != M:
                return True
    else:
        return False


def find_top():
    global arr
    arr2 = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            tmp = 0
            for k in range(4):
                ni = i+di[k]
                nj = j+dj[k]
                if 0<=ni<N and 0<=nj<M:
                    if arr[ni][nj] == 0:
                        tmp += 1
            if tmp >= arr[i][j]:
                arr2[i][j] = 0
            else:
                arr2[i][j] -= tmp
    arr = arr2
    print(arr)
    return





di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
tmp = False
while True:
    check = find_second()
    if check:
        break
    elif check == False:
        result = 0
        break
    else:
        result += 1
        find_top()
print(result)