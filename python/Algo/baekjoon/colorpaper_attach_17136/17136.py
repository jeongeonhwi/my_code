import sys
sys.stdin = open('input.txt', 'r')


import copy
def check_paper(i,j,k,arr):
    arr2 = copy.deepcopy(arr)
    cnt = 0
    for ki in range(k):
        for kj in range(k):
            ni, nj = i+ki, j+kj
            if 0<=ni<10 and 0<=nj<10 and arr[ni][nj] == 1:
                cnt += arr[ni][nj]
                arr2[ni][nj] = 0
            else:
                return 0
    if cnt == k*k:
        return arr2
    else:
        return 0

# arr = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
arr = [list(map(int, input().split())) for _ in range(10)]
cnt = 0
num = [5,5,5,5,5]
for i in range(10):
    for j in range(10):
        if arr[i][j]:
            for k in [5,4,3,2,1]:
                if num[k-1] == 0:
                    continue
                arr2 = check_paper(i,j,k,arr)
                if type(arr2) == list:
                    cnt+=1
                    arr = arr2
                    num[k-1]-=1
                    break
check = 0
for i in arr:
    check+=i.count(1)
if check:
    cnt = -1
print(cnt)