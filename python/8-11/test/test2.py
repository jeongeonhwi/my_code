import sys
sys.stdin = open('input.txt')
import copy

def func(V, adj_arr):
    stack = 0
    visit = [0]*(V+1)
    answer = []
    start = 1
    visit[start] = 1
    v = start
    answer.append(v)

    # for i in range(V+1):



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    adj_arr = [0*(V+1) for _ in range(V+1)]
    for i in range(E):
        adj_arr[arr[i*2]][arr[i*2+1]] = 1
        adj_arr[arr[i * 2+1]][arr[i * 2]] = 1
    result = func(V, adj_arr)