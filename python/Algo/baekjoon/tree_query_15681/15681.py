import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline





N, R, Q = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    g1,g2 = map(int, input().split())
    arr[g1].append(g2)
    arr[g2].append(g1)
size = [-1]*(N+1)

for _ in range(Q):
    query = int(input())
    print(query)