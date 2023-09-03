'''
조합으로 나눈 뒤에 arr이 1인지 확인하고 1이면 ok 하고
풀었는데 2%를 넘지 못했다. 마을이 4개일때 
2개 2개씩 연결되면 내 코드로는 판단이 안되기 때문이다.
그래서 dfs를 사용해서 확인작업을 거치자 바로 통과됐다.
'''



import sys
sys.stdin = open('input.txt', 'r')

def dfs(start, N, arr, ch):
    stack = []
    visit = [0]*(N+1)
    visit[start] = 1
    town = []
    while True:
        town.append(start)
        for w in range(N+1):
            if arr[start][w] == 1 and visit[w] == 0 and w in ch:
                stack.append(start)
                start = w
                visit[start] = 1
                break
        else:
            if stack:
                start = stack.pop()
            else:
                break
    return town




N = int(input())
people = list(map(int, input().split()))
number = []
for i in range(1, N+1):
    number.append(i)
arr = [[0]*(N+1) for _ in range(N+1)]
for n in range(1, N+1):
    a, *b = list(map(int, input().split()))
    for j in b:
        arr[n][j] = 1
        arr[j][n] = 1
# for i in arr:
#     print(i)
min_v = 100000000
for i in range(1<<N):
    part1 = []
    part2 = set()
    for j in range(N):
        if i&(1<<j):
            part1.append(number[j])
    if len(part1) != 0 and len(part1) != len(number):
        part1 = set(part1)
        part2 = set(number) - part1
        part1 = list(part1)
        part2 = list(part2)
        check = False
        town1 = dfs(part1[0], N, arr, part1)
        town2 = dfs(part2[0], N, arr, part2)
        town1 = set(town1)
        town2 = set(town2)
        town1 = list(town1)
        town2 = list(town2)
        part1.sort()
        town1.sort()
        if part1 != town1:
            check = True
        if part2 != town2:
            check = True
        p1count = 0
        for p1 in part1:
            p1count += people[p1-1]
        p2count = 0
        for p2 in part2:
            p2count += people[p2-1]
        tmpmin = abs(p1count - p2count)
        if tmpmin < min_v and check != True:
            min_v = tmpmin
if min_v == 100000000:
    min_v = -1
print(min_v)