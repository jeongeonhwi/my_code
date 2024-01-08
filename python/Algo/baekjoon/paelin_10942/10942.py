import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

def check_question(s,e):
    fe = (s+e)//2
    if (s+e)%2 == 0:
        for i in range(s, fe):
            if i in mydic[e-i]:
                pass
            else:
                return 0
    else:
        for i in range(s, fe+1):
            if i in mydic[e-i]:
                pass
            else:
                return 0
    return 1

N = int(input())
arr = list(map(int, input().split()))
mydic = dict()
for i in range(N):
    for j in range(N):
        if arr[i] == arr[j]:
            if i not in mydic:
                mydic[i] = set()
                mydic[i].add(j)
            else:
                mydic[i].add(j)

ans = ''

M = int(input())
quest = [list(map(int, input().split())) for _ in range(M)]
for s,e in quest:
    s,e = s-1, e-1
    ans += str(check_question(s,e)) + '\n'
print(ans)