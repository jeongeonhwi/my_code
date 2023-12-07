# import sys
# sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N = int(input())
arr = set()
max_l = 0
for _ in range(N):
    word = tuple(input())
    arr.add(word)
    max_l = max(max_l, len(word))
num = [[] for _ in range(max_l+1)]
for i in arr:
    num[len(i)].append(i)
for i in num:
    i.sort()
for i in num:
    for j in i:
        j = list(j)
        ans = ''.join(j)
        print(ans)