import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

row = input()
col = input()
len_row, len_col = len(row), len(col)
dp = [[(0, '')]*(len_col+1) for _ in range(len_row+1)]
dp_data = [0]*(len_row+1)
for i in range(1,len_row+1):
    for j in range(1,len_col+1):
        if row[i-1] == col[j-1]:
            dp[i][j] = (dp[i-1][j-1][0]+1, dp[i-1][j-1][1]+row[i-1])
        else:
            dp[i][j] = (max(dp[i-1][j], dp[i][j-1]))
            if dp[i-1][j][0] > dp[i][j-1][0]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
print(dp[-1][-1][0])
print(dp[-1][-1][1])