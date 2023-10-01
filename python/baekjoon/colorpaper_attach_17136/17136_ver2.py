import sys
sys.stdin = open('input.txt', 'r')


import copy


arr3 = [list(map(int, input().split())) for _ in range(10)]
arr = copy.deepcopy(arr3)
num = [5,5,5,5,5]
m_list = []
for k in range(5, 0, -1):
    for i in range(10-k+1):
        for j in range(10-k+1):
            if num[k-1] == 0:
                continue
            if arr[i][j]:
                arr2 = copy.deepcopy(arr)
                check = False
                for ii in range(k):
                    for jj in range(k):
                        ni,nj = i+ii, j+jj
                        if arr[ni][nj]:
                            arr2[ni][nj] = 0
                        else:
                            check = True
                            break
                    if check:
                        break
                if not check:
                    arr = copy.deepcopy(arr2)
                    num[k-1] -= 1
ans = 25-sum(num)
c1 = 0
for i in arr:
    c1+=i.count(1)
if c1 == 0:
    m_list.append(ans)

arr = copy.deepcopy(arr3)
num = [5,5,5,5,5]
for k in range(4, 0, -1):
    for i in range(10-k+1):
        for j in range(10-k+1):
            if num[k-1] == 0:
                continue
            if arr[i][j]:
                arr2 = copy.deepcopy(arr)
                check = False
                for ii in range(k):
                    for jj in range(k):
                        ni,nj = i+ii, j+jj
                        if arr[ni][nj]:
                            arr2[ni][nj] = 0
                        else:
                            check = True
                            break
                    if check:
                        break
                if not check:
                    arr = copy.deepcopy(arr2)
                    num[k-1] -= 1
ans2 = 25-sum(num)
c1 = 0
for i in arr:
    c1+=i.count(1)
if c1 == 0:
    m_list.append(ans2)

arr = copy.deepcopy(arr3)
num = [5,5,5,5,5]
for k in range(3, 0, -1):
    for i in range(10-k+1):
        for j in range(10-k+1):
            if num[k-1] == 0:
                continue
            if arr[i][j]:
                arr2 = copy.deepcopy(arr)
                check = False
                for ii in range(k):
                    for jj in range(k):
                        ni,nj = i+ii, j+jj
                        if arr[ni][nj]:
                            arr2[ni][nj] = 0
                        else:
                            check = True
                            break
                    if check:
                        break
                if not check:
                    arr = copy.deepcopy(arr2)
                    num[k-1] -= 1
ans3 = 25-sum(num)
c1 = 0
for i in arr:
    c1+=i.count(1)
if c1 == 0:
    m_list.append(ans3)

arr = copy.deepcopy(arr3)
num = [5,5,5,5,5]
for k in range(2, 0, -1):
    for i in range(10-k+1):
        for j in range(10-k+1):
            if num[k-1] == 0:
                continue
            if arr[i][j]:
                arr2 = copy.deepcopy(arr)
                check = False
                for ii in range(k):
                    for jj in range(k):
                        ni,nj = i+ii, j+jj
                        if arr[ni][nj]:
                            arr2[ni][nj] = 0
                        else:
                            check = True
                            break
                    if check:
                        break
                if not check:
                    arr = copy.deepcopy(arr2)
                    num[k-1] -= 1
ans4 = 25-sum(num)
c1 = 0
for i in arr:
    c1+=i.count(1)
if c1 == 0:
    m_list.append(ans4)

arr = copy.deepcopy(arr3)
num = [5,5,5,5,5]
for k in range(2, 0, -1):
    for i in range(10-k+1):
        for j in range(10-k+1):
            if num[k-1] == 0:
                continue
            if arr[i][j]:
                arr2 = copy.deepcopy(arr)
                check = False
                for ii in range(k):
                    for jj in range(k):
                        ni,nj = i+ii, j+jj
                        if arr[ni][nj]:
                            arr2[ni][nj] = 0
                        else:
                            check = True
                            break
                    if check:
                        break
                if not check:
                    arr = copy.deepcopy(arr2)
                    num[k-1] -= 1
ans5 = 25-sum(num)
c1 = 0
for i in arr:
    c1+=i.count(1)
if c1 == 0:
    m_list.append(ans5)

if m_list:
    min_v = min(m_list)
else:
    min_v = -1
print(min_v)