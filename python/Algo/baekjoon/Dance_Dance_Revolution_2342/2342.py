import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def calculator(a,b):
      if a == b:
            return 1
      if a == 0:
            return 2
      if (a-1)%4 == b%4 or (a+1)%4 == b%4:
            return 3
      else:
            return 4

arr = list(map(int, input().split()))
dp = [[[5*len(arr) for _ in range(5)] for _ in range(5)] for _ in range(len(arr))]
dp[0][0][0] = 0
for i in range(len(arr)-1):
      a = arr[i]
      for left in range(5):
            for right in range(5):
                  dp[i+1][left][a] = min(dp[i+1][left][a], dp[i][left][right] + calculator(right, a))
                  dp[i+1][a][right] = min(dp[i+1][a][right], dp[i][left][right] + calculator(left, a))
min_v = 5*len(arr)
for left in range(5):
      for right in range(5):
            min_v = min(min_v, dp[-1][left][right])
print(min_v)