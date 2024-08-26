import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

N,K = map(int, input().split())
S = input().strip()
si,sj = 0,0
stack = []
flag = True
for s in S:
    if s == 'U':
        si -= 1
    elif s == 'D':
        si += 1
    elif s == 'L':
        sj -= 1
    else:
        sj += 1
    if si == 0 and sj == 0:
        print('YES')
        flag = False
        break
    stack.append((si,sj))
ans = 'NO'
if flag:
    ei,ej = stack.pop()
    for mi,mj in stack:
        if ei != 0 and ej != 0 and mi != 0 and mj != 0 and mi%ei ==0 and mj%ej == 0:
            if mi == -ei*abs(mi//ei) and mj == -ej*abs(mj//ej) and abs(mi//ei) == abs(mj//ej) and abs(mj//ej) < K:
                ans = 'YES'
                print(mi,mj, ei,ej)
        if ei == 0 and mi == 0 and mj%ej == 0:
            if mj == -ej*abs(mj//ej) and abs(mj//ej)<K:
                ans = 'YES'
                print(mi, mj, ei,ej)
        if ej == 0 and mj == 0 and mi%ei == 0:
            if mi == -ei*abs(mi//ei) and abs(mi//ei)<K:
                ans = 'YES'
                print(mi, mj, ei,ej)
    print(ans)