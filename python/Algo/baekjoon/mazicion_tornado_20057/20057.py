import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

# 왼쪽방향일때 (0,-1) 변화된 center기준
left_seven = [(-1,0), (1,0)]
left_one = [(-1,1), (1,1)]
left_two = [(-2,0), (2,0)]
left_ten = [(-1,-1), (1,-1)]
left_five = [(0,-2)]
# 오른쪽방향일때 (0,-1) 변화된 center기준
right_seven = [(-1,0), (1,0)]
right_one = [(-1,-1), (1,-1)]
right_two = [(-2,0), (2,0)]
right_ten = [(-1,1), (1,1)]
right_five = [(0,2)]
# 위쪽방향일때 (0,-1) 변화된 center기준
up_seven = [(0,-1), (0,1)]
up_one = [(1,-1), (1,1)]
up_two = [(0,-2), (0,2)]
up_ten = [(-1,-1), (-1,1)]
up_five = [(-2,0)]
# 위쪽방향일때 (0,-1) 변화된 center기준
down_seven = [(0,-1), (0,1)]
down_one = [(-1,-1), (-1,1)]
down_two = [(0,-2), (0,2)]
down_ten = [(1,-1), (1,1)]
down_five = [(2,0)]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
direction = []
for i in range(1, N):
    direction.append(i)
    direction.append(i)
    if i == N-1:
        direction.append(i)
d_idx = 0
center = [N//2, N//2]
out_sum = 0
# 토네이도 완성
for _ in range(N//2):
    for di,dj in [(0,-1), (1,0), (0,1), (-1,0)]:
        for _ in range(direction[d_idx]):
            center[0] += di
            center[1] += dj
            midsum = arr[center[0]][center[1]]
            if di == 0 and dj == -1:
                tmp_i, tmp_j = center[0], center[1]
                for seven_i, seven_j in left_seven:
                    if 0<=tmp_i+seven_i<N and 0<=tmp_j+seven_j<N:
                        arr[tmp_i+seven_i][tmp_j+seven_j] += int(arr[center[0]][center[1]]*0.07)
                        midsum -= int(arr[center[0]][center[1]]*0.07)
                    else:
                        out_sum += int(arr[center[0]][center[1]]*0.07)
                        midsum -= int(arr[center[0]][center[1]] * 0.07)
                for one_i, one_j in left_one:
                    if 0 <= tmp_i + one_i < N and 0 <= tmp_j + one_j < N:
                        arr[tmp_i+one_i][tmp_j+one_j] += int(arr[center[0]][center[1]]*0.01)
                        midsum -= int(arr[center[0]][center[1]] * 0.01)
                    else:
                        out_sum += int(arr[center[0]][center[1]]*0.01)
                        midsum -= int(arr[center[0]][center[1]] * 0.01)
                for two_i, two_j in left_two:
                    if 0 <= tmp_i + two_i < N and 0 <= tmp_j + two_j < N:
                        arr[tmp_i+two_i][tmp_j+two_j] += int(arr[center[0]][center[1]]*0.02)
                        midsum -= int(arr[center[0]][center[1]] * 0.02)
                    else:
                        out_sum += int(arr[center[0]][center[1]]*0.02)
                        midsum -= int(arr[center[0]][center[1]] * 0.02)
                for ten_i, ten_j in left_ten:
                    if 0 <= tmp_i + ten_i < N and 0 <= tmp_j + ten_j < N:
                        arr[tmp_i+ten_i][tmp_j+ten_j] += int(arr[center[0]][center[1]]*0.1)
                        midsum -= int(arr[center[0]][center[1]] * 0.1)
                    else:
                        out_sum += int(arr[center[0]][center[1]]*0.1)
                        midsum -= int(arr[center[0]][center[1]] * 0.1)
                for five_i, five_j in left_five:
                    if 0 <= tmp_i + five_i < N and 0 <= tmp_j + five_j < N:
                        arr[tmp_i+five_i][tmp_j+five_j] += int(arr[center[0]][center[1]]*0.05)
                        midsum -= int(arr[center[0]][center[1]] * 0.05)
                    else:
                        out_sum += int(arr[center[0]][center[1]]*0.05)
                        midsum -= int(arr[center[0]][center[1]] * 0.05)
                if 0 <= tmp_i + di < N and 0 <= tmp_j + dj < N:
                    arr[tmp_i+di][tmp_j+dj] += midsum
                else:
                    out_sum += midsum
            elif di == 1 and dj == 0:
                tmp_i, tmp_j = center[0], center[1]
                for seven_i, seven_j in down_seven:
                    if 0 <= tmp_i + seven_i < N and 0 <= tmp_j + seven_j < N:
                        arr[tmp_i + seven_i][tmp_j + seven_j] += int(arr[center[0]][center[1]] * 0.07)
                        midsum -= int(arr[center[0]][center[1]] * 0.07)
                    else:
                        out_sum += int(arr[center[0]][center[1]] * 0.07)
                        midsum -= int(arr[center[0]][center[1]] * 0.07)
                for one_i, one_j in down_one:
                    if 0 <= tmp_i + one_i < N and 0 <= tmp_j + one_j < N:
                        arr[tmp_i + one_i][tmp_j + one_j] += int(arr[center[0]][center[1]] * 0.01)
                        midsum -= int(arr[center[0]][center[1]] * 0.01)
                    else:
                        out_sum += int(arr[center[0]][center[1]] * 0.01)
                        midsum -= int(arr[center[0]][center[1]] * 0.01)
                for two_i, two_j in down_two:
                    if 0 <= tmp_i + two_i < N and 0 <= tmp_j + two_j < N:
                        arr[tmp_i + two_i][tmp_j + two_j] += int(arr[center[0]][center[1]] * 0.02)
                        midsum -= int(arr[center[0]][center[1]] * 0.02)
                    else:
                        out_sum += int(arr[center[0]][center[1]] * 0.02)
                        midsum -= int(arr[center[0]][center[1]] * 0.02)
                for ten_i, ten_j in down_ten:
                    if 0 <= tmp_i + ten_i < N and 0 <= tmp_j + ten_j < N:
                        arr[tmp_i + ten_i][tmp_j + ten_j] += int(arr[center[0]][center[1]] * 0.1)
                        midsum -= int(arr[center[0]][center[1]] * 0.1)
                    else:
                        out_sum += int(arr[center[0]][center[1]] * 0.1)
                        midsum -= int(arr[center[0]][center[1]] * 0.1)
                for five_i, five_j in down_five:
                    if 0 <= tmp_i + five_i < N and 0 <= tmp_j + five_j < N:
                        arr[tmp_i + five_i][tmp_j + five_j] += int(arr[center[0]][center[1]] * 0.05)
                        midsum -= int(arr[center[0]][center[1]] * 0.05)
                    else:
                        out_sum += int(arr[center[0]][center[1]] * 0.05)
                        midsum -= int(arr[center[0]][center[1]] * 0.05)
                if 0 <= tmp_i + di < N and 0 <= tmp_j + dj < N:
                    arr[tmp_i + di][tmp_j + dj] += midsum
                else:
                    out_sum += midsum
            elif di == 0 and dj == 1:
                tmp_i, tmp_j = center[0], center[1]
                for seven_i, seven_j in right_seven:
                    if 0 <= tmp_i + seven_i < N and 0 <= tmp_j + seven_j < N:
                        arr[tmp_i + seven_i][tmp_j + seven_j] += int(arr[center[0]][center[1]] * 0.07)
                        midsum -= int(arr[center[0]][center[1]] * 0.07)
                    else:
                        out_sum += int(arr[center[0]][center[1]] * 0.07)
                        midsum -= int(arr[center[0]][center[1]] * 0.07)
                for one_i, one_j in right_one:
                    if 0 <= tmp_i + one_i < N and 0 <= tmp_j + one_j < N:
                        arr[tmp_i + one_i][tmp_j + one_j] += int(arr[center[0]][center[1]] * 0.01)
                        midsum -= int(arr[center[0]][center[1]] * 0.01)
                    else:
                        out_sum += int(arr[center[0]][center[1]] * 0.01)
                        midsum -= int(arr[center[0]][center[1]] * 0.01)
                for two_i, two_j in right_two:
                    if 0 <= tmp_i + two_i < N and 0 <= tmp_j + two_j < N:
                        arr[tmp_i + two_i][tmp_j + two_j] += int(arr[center[0]][center[1]] * 0.02)
                        midsum -= int(arr[center[0]][center[1]] * 0.02)
                    else:
                        out_sum += int(arr[center[0]][center[1]] * 0.02)
                        midsum -= int(arr[center[0]][center[1]] * 0.02)
                for ten_i, ten_j in right_ten:
                    if 0 <= tmp_i + ten_i < N and 0 <= tmp_j + ten_j < N:
                        arr[tmp_i + ten_i][tmp_j + ten_j] += int(arr[center[0]][center[1]] * 0.1)
                        midsum -= int(arr[center[0]][center[1]] * 0.1)
                    else:
                        out_sum += int(arr[center[0]][center[1]] * 0.1)
                        midsum -= int(arr[center[0]][center[1]] * 0.1)
                for five_i, five_j in right_five:
                    if 0 <= tmp_i + five_i < N and 0 <= tmp_j + five_j < N:
                        arr[tmp_i + five_i][tmp_j + five_j] += int(arr[center[0]][center[1]] * 0.05)
                        midsum -= int(arr[center[0]][center[1]] * 0.05)
                    else:
                        out_sum += int(arr[center[0]][center[1]] * 0.05)
                        midsum -= int(arr[center[0]][center[1]] * 0.05)
                if 0 <= tmp_i + di < N and 0 <= tmp_j + dj < N:
                    arr[tmp_i + di][tmp_j + dj] += midsum
                else:
                    out_sum += midsum
            elif di == -1 and dj == 0:
                tmp_i, tmp_j = center[0], center[1]
                for seven_i, seven_j in up_seven:
                    if 0 <= tmp_i + seven_i < N and 0 <= tmp_j + seven_j < N:
                        arr[tmp_i + seven_i][tmp_j + seven_j] += int(arr[center[0]][center[1]] * 0.07)
                        midsum -= int(arr[center[0]][center[1]] * 0.07)
                    else:
                        out_sum += int(arr[center[0]][center[1]] * 0.07)
                        midsum -= int(arr[center[0]][center[1]] * 0.07)
                for one_i, one_j in up_one:
                    if 0 <= tmp_i + one_i < N and 0 <= tmp_j + one_j < N:
                        arr[tmp_i + one_i][tmp_j + one_j] += int(arr[center[0]][center[1]] * 0.01)
                        midsum -= int(arr[center[0]][center[1]] * 0.01)
                    else:
                        out_sum += int(arr[center[0]][center[1]] * 0.01)
                        midsum -= int(arr[center[0]][center[1]] * 0.01)
                for two_i, two_j in up_two:
                    if 0 <= tmp_i + two_i < N and 0 <= tmp_j + two_j < N:
                        arr[tmp_i + two_i][tmp_j + two_j] += int(arr[center[0]][center[1]] * 0.02)
                        midsum -= int(arr[center[0]][center[1]] * 0.02)
                    else:
                        out_sum += int(arr[center[0]][center[1]] * 0.02)
                        midsum -= int(arr[center[0]][center[1]] * 0.02)
                for ten_i, ten_j in up_ten:
                    if 0 <= tmp_i + ten_i < N and 0 <= tmp_j + ten_j < N:
                        arr[tmp_i + ten_i][tmp_j + ten_j] += int(arr[center[0]][center[1]] * 0.1)
                        midsum -= int(arr[center[0]][center[1]] * 0.1)
                    else:
                        out_sum += int(arr[center[0]][center[1]] * 0.1)
                        midsum -= int(arr[center[0]][center[1]] * 0.1)
                for five_i, five_j in up_five:
                    if 0 <= tmp_i + five_i < N and 0 <= tmp_j + five_j < N:
                        arr[tmp_i + five_i][tmp_j + five_j] += int(arr[center[0]][center[1]] * 0.05)
                        midsum -= int(arr[center[0]][center[1]] * 0.05)
                    else:
                        out_sum += int(arr[center[0]][center[1]] * 0.05)
                        midsum -= int(arr[center[0]][center[1]] * 0.05)
                if 0 <= tmp_i + di < N and 0 <= tmp_j + dj < N:
                    arr[tmp_i + di][tmp_j + dj] += midsum
                else:
                    out_sum += midsum
        d_idx+=1
else:
    di, dj = [0, -1]
    for _ in range(direction[d_idx]):
        center[0] += di
        center[1] += dj
        tmp_i, tmp_j = center[0], center[1]
        midsum = arr[center[0]][center[1]]
        for seven_i, seven_j in left_seven:
            if 0 <= tmp_i + seven_i < N and 0 <= tmp_j + seven_j < N:
                arr[tmp_i + seven_i][tmp_j + seven_j] += int(arr[center[0]][center[1]] * 0.07)
                midsum -= int(arr[center[0]][center[1]] * 0.07)
            else:
                out_sum += int(arr[center[0]][center[1]] * 0.07)
                midsum -= int(arr[center[0]][center[1]] * 0.07)
        for one_i, one_j in left_one:
            if 0 <= tmp_i + one_i < N and 0 <= tmp_j + one_j < N:
                arr[tmp_i + one_i][tmp_j + one_j] += int(arr[center[0]][center[1]] * 0.01)
                midsum -= int(arr[center[0]][center[1]] * 0.01)
            else:
                out_sum += int(arr[center[0]][center[1]] * 0.01)
                midsum -= int(arr[center[0]][center[1]] * 0.01)
        for two_i, two_j in left_two:
            if 0 <= tmp_i + two_i < N and 0 <= tmp_j + two_j < N:
                arr[tmp_i + two_i][tmp_j + two_j] += int(arr[center[0]][center[1]] * 0.02)
                midsum -= int(arr[center[0]][center[1]] * 0.02)
            else:
                out_sum += int(arr[center[0]][center[1]] * 0.02)
                midsum -= int(arr[center[0]][center[1]] * 0.02)
        for ten_i, ten_j in left_ten:
            if 0 <= tmp_i + ten_i < N and 0 <= tmp_j + ten_j < N:
                arr[tmp_i + ten_i][tmp_j + ten_j] += int(arr[center[0]][center[1]] * 0.1)
                midsum -= int(arr[center[0]][center[1]] * 0.1)
            else:
                out_sum += int(arr[center[0]][center[1]] * 0.1)
                midsum -= int(arr[center[0]][center[1]] * 0.1)
        for five_i, five_j in left_five:
            if 0 <= tmp_i + five_i < N and 0 <= tmp_j + five_j < N:
                arr[tmp_i + five_i][tmp_j + five_j] += int(arr[center[0]][center[1]] * 0.05)
                midsum -= int(arr[center[0]][center[1]] * 0.05)
            else:
                out_sum += int(arr[center[0]][center[1]] * 0.05)
                midsum -= int(arr[center[0]][center[1]] * 0.05)
        if 0 <= tmp_i + di < N and 0 <= tmp_j + dj < N:
            arr[tmp_i + di][tmp_j + dj] += midsum
        else:
            out_sum += midsum
print(out_sum)