a = [1,2,3,4]
from itertools import combinations, permutations

from collections import deque
from heapq import heappush, heappop

# for combi in combinations(a, 2):
#     print(combi)

# for permu in permutations(a,3):
#     print(permu)

# b = deque(a)
# print(b)

# c = []
# heappush(c, 2)
# heappush(c, 1)
# heappush(c, 3)
# print(heappop(c))

# from bisect import bisect, bisect_left, bisect_right
#
# print(bisect(a, 6))

# from math import sqrt
#
# print(sqrt(3))

# print(abs(-1))

# print(round(3.161, 1))

# parent = [i for i in range(10)]
#
# def find_parent(x):
#     if x == parent[x]:
#         return x
#     parent[x] = find_parent(parent[x])
#     return parent[x]
#
#
# def union(x, y):
#     x = find_parent(x)
#     y = find_parent(y)
#     if x<y:
#         parent[y] = x
#     else:
#         parent[x] = y
#
# union(2,3)
# union(3,4)
# union(6,7)
# union(4,7)
# for i in range(10):
#     find_parent(i)
# print(parent)

# d = dict()
# d[1] = 2
# print(d)

# print(list('abcd'))

# print(ord('a'), chr(97))
# print(ord('A'), chr(65))
# print(ord('0'), ord('9'))
# for i in range(ord('a'), ord('z')+1):
#     print(chr(i))

