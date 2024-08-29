import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def have_bishop(c, s, e,bp):
    global max_v
    if c+(e-s) <= max_v:
        return
    for b in range(s, e):
        i,j = bp[b]
        if not diag1[i + j] and not diag2[i - j + N - 1]:
            diag1[i+j] = diag2[i-j + N -1] = True
            have_bishop(c+1, b+1, e, bp)
            diag1[i+j] = diag2[i-j+N-1] = False
    max_v = max(max_v, c)

def solve(bp):
    global max_v
    max_v = 0
    have_bishop(0, 0, len(bp), bp)
    return max_v

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
diag1 = [False] * (2 * N - 1)
diag2 = [False] * (2 * N - 1)
bp_black = []
bp_white = []
max_b = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            if (i + j) % 2 == 0:
                bp_black.append((i, j))
            else:
                bp_white.append((i, j))

ans = solve(bp_black)+solve(bp_white)
print(ans)