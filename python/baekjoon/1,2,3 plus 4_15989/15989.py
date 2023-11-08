import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    n = int(input())
    dp = 0
    level = 0
    for i in range(1, n+1):
        if i%6 == 1:
            level+=1
        dp += level
        if i%6 == 0:
            dp += 1
        elif i%6 == 1:
            dp -= 1
    print(dp+1)