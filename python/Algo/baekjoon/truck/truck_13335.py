import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

from collections import deque
# n = 트럭의 수, w = 다리의 길이 l = 최대하중
n,w,l = map(int, input().split())
truck = list(map(int, input().split()))
total_time = 0
truck_cnt = 0
bridge = [0]*w
bridge = deque(bridge)
n_cnt = 0
while True:
    total_time += 1
    if bridge[-1] != 0:
        n_cnt+=1
        bridge[-1] = 0
    if n_cnt == n:
        break
    bridge.rotate(1)
    weight = 0
    weight += sum(bridge)
    if truck_cnt < n:
        if weight+truck[truck_cnt] <= l:
            bridge[0] = truck[truck_cnt]
            truck_cnt+=1


print(total_time)