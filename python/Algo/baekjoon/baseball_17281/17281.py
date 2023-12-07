import sys
sys.stdin = open('input.txt', 'r')
from itertools import permutations
import copy
# 0과 3번 인덱스는 교체한채 3번 인덱스 고정
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
num = [1, 2, 3, 4, 5, 6, 7, 8]
eight = 8
used = [0] * 8
p = [0] * 8
score = 0
for p in permutations(num, eight):
    p = list(p)
    nu = p[:3] + [0] + p[3:]
    outpoint = 0
    current = 0
    ru1 = False
    ru2 = False
    ru3 = False
    ining = 0
    tmpscore = 0
    while ining < N:
        if arr[ining][nu[current % 9]] == 0:
            outpoint += 1
            current += 1
        elif arr[ining][nu[current % 9]] == 1:
            if ru1:
                if ru2:
                    if ru3:
                        tmpscore += 1
                    else:
                        ru3 = True
                else:
                    ru2 = True
                    if ru3:
                        tmpscore += 1
                        ru3 = False
            else:
                ru1 = True
                if ru2:
                    if ru3:
                        tmpscore += 1
                        ru2 = False
                    else:
                        ru3 = True
                        ru2 = False
                else:
                    if ru3:
                        tmpscore += 1
                        ru3 = False
            current += 1
        elif arr[ining][nu[current % 9]] == 2:
            if ru2:
                tmpscore += 1
            else:
                ru2 = True
            if ru3:
                tmpscore += 1
                if ru1:
                    ru1 = False
                else:
                    ru3 = False
            else:
                if ru1:
                    ru3 = True
                    ru1 = False
            current += 1
        elif arr[ining][nu[current % 9]] == 3:
            if ru1:
                tmpscore += 1
                ru1 = False
            if ru2:
                tmpscore += 1
                ru2 = False
            if ru3:
                tmpscore += 1
            else:
                ru3 = True
            current += 1
        elif arr[ining][nu[current % 9]] == 4:
            if ru1:
                tmpscore += 1
                ru1 = False
            if ru2:
                tmpscore += 1
                ru2 = False
            if ru3:
                tmpscore += 1
                ru3 = False
            tmpscore += 1
            current += 1
        if outpoint >= 3:
            ining += 1
            outpoint = 0
            if ru1:
                ru1 = False
            if ru2:
                ru2 = False
            if ru3:
                ru3 = False
    if tmpscore > score:
        score = tmpscore
print(score)
