import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
# 11
# 임의의 한점에서 가장 먼 노드는 그 노드에서 가장 먼 노드가 트리의 지름이다.

from heapq import heappush,heappop

def priority_queue(sn):
    global max_v
    visited = [0]*(V+1)
    hq = [[0,sn,0]]
    far_node = 0
    total_cost = 0
    while hq:
        cnt, node, weight = heappop(hq)
        for cost, nextnode in arr[node]:
            if visited[nextnode] == 0:
                visited[node] = 1
                heappush(hq, [cost, nextnode, weight-cost])
                if total_cost < weight-cost:
                    total_cost = weight-cost
                    far_node = nextnode
    # print(total_cost)
    return total_cost,far_node

V = int(input())
arr = [[] for _ in range(V+1)]
a = []
for v in range(V):
    node_info = list(map(int, input().split()))
    for i in range(1, len(node_info)-1):
        if i%2==1:
            arr[node_info[0]].append([-node_info[i+1],node_info[i]])

total_cost, far_node = priority_queue(1)
max_v, node = priority_queue(far_node)
print(max_v)