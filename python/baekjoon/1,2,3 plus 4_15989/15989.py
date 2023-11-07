import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline


T = int(input())
for _ in range(T):
    n = int(input())
    dp = 4
    if n > 4:
        for i in range(5, n+1):
            if i%2 == 1:
                if i%3 == 0:
                    dp += 2
                else:
                    if i > 10:
                        dp += 2
                    else:
                        dp += 1
            else:
                dp += 2
            if i%5==0 and i%7==0:
                dp += 2
    elif n == 4:
        dp = 4
    elif n == 3:
        dp = 3
    elif n == 2:
        dp = 2
    elif n == 1:
        dp = 1
    print(dp)