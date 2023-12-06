import sys
sys.stdin = open('input.txt', 'r')


from collections import deque
T = int(input())
for _ in range(T):
    N, turn = map(int, input().split())
    arr = list(map(int, input().split()))
    check = deque()
    for i in range(N):
        if i == turn:
            check.append((arr[i], True))
            continue
        check.append((arr[i], False))
    result = 0
    while True:
        tmp = check[0][0]
        next = False
        for i in check:
            if tmp < i[0]:
                next = True
                break
        if next:
            check.rotate(-1)
            continue
        tmp = check.popleft()
        if tmp[1]:
            result+=1
            print(result)
            break
        else:
            result+=1