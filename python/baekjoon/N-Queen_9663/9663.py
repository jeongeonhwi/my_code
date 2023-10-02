'''
문제접근 1. 순열과 find함수를 만들어 해결하려 했으나
시간초과가 날 확률이 너무 크다.
문제접근 2. 각행에 1개씩 퀸이 들어가고 맨 끝부터 몇개가
끝까지 도착할 수 있는지 dfs로 접근하면 될것같다.
문제접근 3. 지금은 내가 약해서 물러나지만 다음에는 풀자
'''


import sys
# sys.stdout = open('output.txt', 'w')


def permutation(start, end):
    if start == end:
        c = tuple(p)
        my_set.add(c)
        return
    for j in range(end):
        if used[j] == 0:
            p[start] = num[j]
            used[j] = 1
            permutation(start+1, end)
            used[j] = 0


def find_Q(ntuple):
    global cnt
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        arr[i][ntuple[i]] = 2

N = int(input())
num = [i for i in range(N)]
p = [0]*N
used = [0]*N
my_set = set()
permutation(0, N)
cnt = 0
for i in my_set:
    find_Q(i)