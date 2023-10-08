import sys
sys.stdin = open('input.txt', 'r')

from collections import deque
N,K = map(int, input().split())
arr = list(map(int, input().split()))
robot = []
ans = 0
while True:
    ans += 1
    # 컨테이너 이동
    next = arr.pop()
    arr = [next]+arr
    # 로봇 이동
    for i in range(len(robot)):
        robot[i] += 1
        if robot[i] == N-1:
            robot[i] = -1
    tmp = []
    for i in robot:
        if i == -1:
            continue
        tmp.append(i)
    robot = tmp[:]
    # 한칸더 갈수 있으면 가기
    tmp = []
    robot.sort()
    while robot:
        i = robot.pop()
        if i+1 == N-1 and arr[i+1] >= 1:
            arr[i+1] -= 1
            continue
        if arr[i+1] >= 1 and i+1 not in robot and i+1 not in tmp:
            arr[i+1] -= 1
            tmp.append(i+1)
            continue
        tmp.append(i)
    if arr[0]:
        arr[0] -= 1
        tmp.append(0)
    robot = tmp[:]
    if arr.count(0) >= K:
        break
print(ans)