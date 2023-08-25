import sys
sys.stdin = open('input.txt', 'r')
# 여학생은 0, 남학생은 1
T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    group = [0]*12
    for _ in range(N):
        S, Y = map(int, input().split())
        if S == 0:
            group[2*(Y-1)] += 1
        else:
            group[2*(Y-1)+1] += 1
    count = 0
    for num in range(len(group)):
        if group[num] != 0 and group[num] <= K:
            count += 1
            group[num] = 0
    for num in group:
        count += num//K
        if num%K != 0:
            count += 1
    print(count)
