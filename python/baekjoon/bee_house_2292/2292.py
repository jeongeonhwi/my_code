import sys
input = sys.stdin.readline

N = int(input())
level = 1
tmp = 1
while True:
    tmp += level*6
    if N == 1:
        print(1)
        break
    if N <= tmp:
        print(level+1)
        break
    level+=1