import sys
sys.stdin = open('input.txt')


# 1은 가위    2는 바위    3은 보
T = int(input())
for tc in range(1, T+1):
    dic = {}
    N = int(input())
    arr = list(map(int, input().split()))
    num = []
    for i in range(1,N+1):
        dic[i] = arr[i-1]
        num.append(i)
    while True:
        pass