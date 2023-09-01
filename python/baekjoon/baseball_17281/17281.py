import sys
sys.stdin = open('input.txt', 'r')

def sunyeol(i, eight):
    if i == eight:
        c = p[:]
        numbers.append(c)
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
arr = []
for _ in range(N):
    a = list(map(int, input().split()))
    arr.append(a)
num = [1, 2, 3, 4, 5, 6, 7, 8]
eight = 8
used = [0] * 8
p = [0] * 8
numbers = []
sunyeol(0, eight)
score = 0
for i in range(len(numbers)):
    outpoint = 0
    current = 0%8
    ground = []
    for j in range(len(numbers[i])):
        for n in range(N):
            if arr[n][numbers[i][j]] == 0:
                outpoint += 1
            elif arr[n][numbers[i][j]] == 1:
                if len(ground) == 3:
                    score += 1
                    ground = [1, 2, 3]
                elif len(ground) == 2:
                    if 1 in ground and 2 in ground:
                        ground = [1, 2, 3]
                    elif 1 in ground and 3 in ground:
                        score += 1
                        ground = [1, 2]
                    elif 2 in ground and 3 in ground:
                        score += 1
                        ground = [1, 3]
            elif arr[n][numbers[i][j]] == 2:
                # 여기까지 세부적인 조건 넣다가 그만둠
                if len(ground) == 3:
                    score += 2
                    ground = [2, 3]
                elif len(ground) == 2:
                    if 1 in ground and 2 in ground:
                        ground = [1, 2, 3]
                    elif 1 in ground and 3 in ground:
                        score += 1
                        ground = [1, 2]
                    elif 2 in ground and 3 in ground:
                        score += 1
                        ground = [1, 3]
            elif arr[n][numbers[i][j]] == 3:
                ground.append(3)
