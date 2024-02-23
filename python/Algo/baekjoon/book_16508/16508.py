import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
from collections import Counter

text = input().strip()
n = int(input())
ndic = dict()
for nn in text:
    if nn in ndic:
        ndic[nn] += 1
    else:
        ndic[nn] = 1
cost = []
for _ in range(n):
    c,d = map(str, input().split())
    cost.append((int(c), d))

ans = float('inf')

def dfs(word, i, c):
    global ans
    if c >= ans:
        return
    if i == n:
        if word == '':
            return
        check = 0
        word = Counter(word)
        for dd in ndic:
            if ndic[dd] <= word[dd]:
                check += 1
            else:
                return
        if check == len(ndic):
            ans = min(ans, c)
        return
    dfs(word+cost[i][1], i+1, c+cost[i][0])
    dfs(word, i+1, c)

dfs('',0,0)

if ans == float('inf'):
    print(-1)
else:
    print(ans)