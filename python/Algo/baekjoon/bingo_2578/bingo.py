import sys
sys.stdin = open('input.txt')


def bingo(arr, host):
    for i in range(5):
        for j in range(5):
            a = host[i][j]
            for di in range(5):
                for dj in range(5):
                    if arr[di][dj] == a:
                        arr[di][dj] = 0
            total = 0
            for ki in range(5):
                count = 0
                for kj in range(5):
                    if arr[ki][kj] == 0:
                        count += 1
                if count == 5:
                    total += 1
            for tj in range(5):
                count1 = 0
                for ti in range(5):
                    if arr[ti][tj] == 0:
                        count1 += 1
                if count1 == 5:
                    total += 1
            count2 = 0
            for ki in range(5):
                if arr[ki][ki] == 0:
                    count2 += 1
            if count2 == 5:
                total += 1

            count3 = 0
            for ki in range(5):
                if arr[ki][4-ki] == 0:
                    count3 += 1
            if count3 == 5:
                total += 1

            if total >= 3:
                return i*5+j+1

arr = [list(map(int, input().split())) for _ in range(5)]
host = [list(map(int, input().split())) for _ in range(5)]
ans = bingo(arr, host)
print(ans)
