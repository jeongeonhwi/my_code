import sys
sys.stdin = open('input.txt', 'r')


def dfs1(start):
    visited1 = [0]*N
    visited1[start] = 1
    stack = [start]
    while stack:
        i = stack.pop()
        for j in arr[i]:
            if visited1[j] == 0 and j in group1:
                visited1[j] = 1
                stack.append(j)
    return visited1

def dfs2(start):
    visited2 = [0]*N
    visited2[start] = 1
    stack = [start]
    while stack:
        i = stack.pop()
        for j in arr[i]:
            if visited2[j] == 0 and j in group2:
                visited2[j] = 1
                stack.append(j)
    return visited2

N = int(input())
people = list(map(int, input().split()))
num = [i for i in range(N)]
arr = [[] for _ in range(N)]
my_num = set(num)
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(1,len(tmp)):
        arr[i].append(tmp[j]-1)
min_v = 100000000
for i in range(1<<N):
    group1 = set()
    for j in range(N):
        if i & (1<<j):
            group1.add(num[j])
    if len(group1) ==0 or len(group1) == N:
        continue
    group2 = my_num - group1
    tmp1 = group1.pop()
    visited1 = dfs1(tmp1)
    group1.add(tmp1)
    check1 = 0
    for gr in group1:
        if visited1[gr] == 1:
            check1 += 1
    if check1 != len(group1):
        continue
    tmp2 = group2.pop()
    visited2 = dfs2(tmp2)
    group2.add(tmp2)
    check2 = 0
    for gr in group2:
        if visited2[gr] == 1:
            check2+=1
    if check2 != len(group2):
        continue
    ans1, ans2 = 0,0
    for gr in group1:
        ans1 += people[gr]
    for gr in group2:
        ans2 += people[gr]
    min_v = min(min_v, abs(ans1-ans2))

if min_v == 100000000:
    min_v = -1
print(min_v)