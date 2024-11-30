import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    mi, mj = 100001, 100001
    for _ in range(N):
        a,b = map(int, input().split())
        stack = []
        if a < mi and b < mj:
            mi,mj = a,b
            tmp = []
            while stack:
                i,j = stack.pop()
                if mi < i and mj < j:
                    continue
                tmp.append((i,j))
            stack = tmp
        else:
            if a <= mi or b <= mj:
                stack.append((a,b))
    print(len(stack))