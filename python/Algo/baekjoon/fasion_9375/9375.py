import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
from itertools import combinations


t = int(input())
for _ in range(t):
    n = int(input())
    d = dict()
    k = []
    for _ in range(n):
        a = list(input().split())
        if a[1] in d:
            d[a[1]] += 1
        else:
            d[a[1]] = 1
            k.append(a[1])
    c = 0
    for i in range(1,len(k)+1):
        for combi in combinations(k, i):
            tc = 1
            for key in combi:
                tc*= d[key]
            c+=tc
    print(c)