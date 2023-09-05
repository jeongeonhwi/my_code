import sys
sys.stdin = open('input.txt', 'r')


def sunyeol(i, eight):
    global score
    if i == eight:
        nu = p[:]
        tmparr = []
        for i in range(len(arr)):
            tmp = []
            for n in range(10):
                for nuu in range(len(nu)):
                    if n == nu[nuu]:
                        tmp.append(arr[i][nuu + 1])
            tmp = tmp[:3] + [arr[i][0]] + tmp[3:]
            tmparr.append(tmp)
        outpoint = 0
        current = 0
        ru1 = False
        ru2 = False
        ru3 = False
        ining = 0
        tmpscore = 0
        while ining < N:
            if tmparr[ining][current % 9] == 0:
                outpoint += 1
                current += 1
            elif tmparr[ining][current % 9] == 1:
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
            elif tmparr[ining][current % 9] == 2:
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
            elif tmparr[ining][current % 9] == 3:
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
            elif tmparr[ining][current % 9] == 4:
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
        return
    else:
        for j in range(eight):
            if used[j] == 0:
                p[i] = num[j]
                used[j] = 1
                sunyeol(i+1, eight)
                used[j] = 0


# 0과 3번 인덱스는 교체한채 3번 인덱스 고정
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)
num = [1, 2, 3, 4, 5, 6, 7, 8]
eight = 8
used = [0] * 8
p = [0] * 8
numbers = []
score = 0
sunyeol(0, eight)
print(score)
