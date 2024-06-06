import sys
sys.setrecursionlimit(10**5)

def boolean_visited(row, col):
    if col_check[col] or left_diag_check[row - col + N - 1] or right_diag_check[row + col]:
        return False
    return True

def jegi(row):
    global cnt
    if row == N:
        cnt += 1
        return
    for col in range(N):
        if boolean_visited(row, col):
            col_check[col] = left_diag_check[row - col + N - 1] = right_diag_check[row + col] = True
            jegi(row + 1)
            col_check[col] = left_diag_check[row - col + N - 1] = right_diag_check[row + col] = False

N = int(input())
cnt = 0
# col의 여부를 확인
col_check = [False] * N
# 왼쪽 아래에서 오른쪽 위를 향하는 대각선 체크
left_diag_check = [False] * (2 * N - 1)
# 왼쪽 위에서 오른쪽 아래를 향하는 대각선 체크
right_diag_check = [False] * (2 * N - 1)

jegi(0)
print(cnt)
