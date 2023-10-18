import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
sys.setrecursionlimit(10000)



def f(start, end, cnt):
    global max_v
    if start >= end:
        max_v = max(max_v, cnt)
        return
    if start < N:
        f(start+day_list[start],end, cnt+pay_list[start])
    else:
        max_v = max(max_v, cnt)
        return
    f(start+1,end,cnt)




N = int(input())
max_v = 0
day_list = []
pay_list = []
for _ in range(N):
    day, pay = map(int, input().split())
    day_list.append(day-1)
    pay_list.append(pay)
f(0,N,0)
print(max_v)