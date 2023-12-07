import sys

input = sys.stdin.readline

def func(row, col, cnt):
    global ans
    if col >= 10:
        ans = min(ans, cnt)
        return

    if row >= 10:
        func(0, col+1, cnt)
        return

    if arr[row][col] == 1:
        for k in range(5):
            if paper[k] == 5:
                continue
            if row + k >= 10 or col + k >= 10:
                continue

            check = False
            for i in range(row, row + k + 1):
                for j in range(col, col + k + 1):
                    if arr[i][j] == 0:
                        check = True
                        break
                if check:
                    break

            if not check:
                for i in range(row, row + k + 1):
                    for j in range(col, col + k + 1):
                        arr[i][j] = 0

                paper[k] += 1
                func(row + k + 1, col, cnt + 1)
                paper[k] -= 1

                for i in range(row, row + k + 1):
                    for j in range(col, col + k + 1):
                        arr[i][j] = 1
    else:
        func(row + 1, col, cnt)


arr = [list(map(int, input().split())) for _ in range(10)]
paper = [0]*5
ans = 50
func(0, 0, 0)
if ans == 50:
    ans = -1
print(ans)