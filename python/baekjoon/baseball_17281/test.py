import sys
sys.stdin = open('input.txt', 'r')


a = [8, 7, 6, 5, 4, 3, 2, 1]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

a = a[:2] + [100] + a[3:]
print(a)
# tmparr = []
# for i in range(len(arr)):
#     # print(arr[i])
#     tmp = []
#     for n in range(10):
#         for nuu in range(len(a)):
#             if n == a[nuu]:
#                 if n == 3:
#                     tmp.append(arr[i][0])
#                 tmp.append(arr[i][nuu+1])
#     tmparr.append(tmp)
# print(tmparr)