import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def dfs(si):
    global label, solo
    memory_arr = [si]
    stack = [si]
    visited[si] = label
    while stack:
        i = stack.pop()
        ni = arr[i]
        if visited[ni] == 0:
            visited[ni] = label
            memory_arr.append(ni)
            stack.append(ni)
        elif visited[ni] == label:
            solo += check_arr(ni,memory_arr)
            label += 1
        else:
            solo += len(memory_arr)
            label += 1

def check_arr(ni, memory_arr):
    while memory_arr:
        i = memory_arr.pop()
        if ni == i:
            return len(memory_arr)
    return 0

T = int(input())
for _ in range(T):
    N = int(input())
    arr =[0]+ list(map(int, input().split()))
    visited = [0]*(N+1)
    solo = 0
    label = 1
    for i in range(1, N+1):
        if visited[i] == 0:
            dfs(i)
    print(solo)