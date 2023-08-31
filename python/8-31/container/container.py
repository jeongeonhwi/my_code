import sys
sys.stdin = open('input.txt', 'r')





T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    capacity = list(map(int, input().split()))
    we_part = []
    we_part2 = []
    for i in range(1<<N):
        tmp = []
        for j in range(i):
            if i&(1<<j):
                tmp.append(weight[j])
        tmp1 = []
        tmp2 = []
        for j in weight:
            if j in tmp:
                tmp1.append(j)
            else:
                tmp2.append(j)
        we_part.append(tmp1)
        we_part2.append(tmp2)
    total = 0
    for i in range(len(we_part)):
        if sum(we_part[i]) <= capacity[0] and sum(we_part2[i]) <= capacity[1]:
            count = len(we_part) + len(we_part2)
            if count > total:
                total = count
    print(total)