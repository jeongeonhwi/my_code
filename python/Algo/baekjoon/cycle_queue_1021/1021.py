from collections import deque

N,M = map(int, input().split())
arr = list(map(int, input().split()))
num = [i for i in range(1,N+1)]
num = deque(num)
cnt = 0
for a in arr:
    left_move = num.copy()
    right_move = num.copy()
    c = 0
    while True:
        if left_move[0] == a:
            cnt+=c
            left_move.popleft()
            num = left_move.copy()
            break
        elif right_move[0] == a:
            cnt+=c
            right_move.popleft()
            num = right_move.copy()
            break
        left_move.rotate(-1)
        right_move.rotate(1)
        c+=1
print(cnt)