import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def jegi():
    global ans
    if a == b:
        ans = 1
        return
    if ans == 1:
        return
    if len(b) < len(a):
        return
    if b[-1] == 'A':
        b.pop()
        jegi()
        b.append('A')
    if b[0] == 'B':
        b.reverse()
        b.pop()
        jegi()
        b.append('B')
        b.reverse()



a = list(input().strip())
b = list(input().strip())

ans = 0
jegi()
print(ans)