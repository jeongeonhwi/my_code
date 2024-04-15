import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

# T,W = map(int, input().split())
# tree = []
# saveData = 0
# cnt = 0
# for _ in range(T):
#     data = int(input())
#     if saveData == 0:
#         saveData = data
#         cnt = 1
#     else:
#         if data == saveData:
#             cnt += 1
#         else:
#             tree.append((saveData, cnt))
#             cnt = 1
#             saveData = data
# tree.append((saveData,cnt))
#
# dp = [[0]*len(tree) for _ in range(3)]
# if tree[0][0] == 1:
#     dp[1][0] = ()
# for i in range(1, len(tree)):


T,W = map(int, input().split())
tree = [int(input()) for _ in range(T)]

dp = [[[(0,0)]*3 for _ in range(W)] for _ in range(T)]

for t in range(T):
    