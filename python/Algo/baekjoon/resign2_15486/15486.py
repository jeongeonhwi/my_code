import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline
sys.setrecursionlimit(1000)



def f(start, end, cnt):
    global max_v
    max_list[start] = max(max_list[start],max_list[start-1])
    max_list[start] = max(max_list[start], max(max_list[start], max_list[start-1]+cnt))
    if start >= end:
        max_v = max(max_v, cnt)
        return
    if day[start] == 1:
        f(start + day_list[start], end, cnt + pay_list[start])
    else:
        if start < N+1:
            if start+day_list[start] <= N+1:
                f(start+day_list[start],end, cnt+pay_list[start])
            else:
                max_v = max(max_v, cnt)
        else:
            max_v = max(max_v, cnt)
            return
        f(start+1,end,cnt)




N = int(input())
max_v = 0
max_list = [0]*(N+1)
day_list = [0]*(N+1)
pay_list = [0]*(N+1)
for i in range(1,N+1):
    day, pay = map(int, input().split())
    day_list[i] = day
    pay_list[i] = pay
f(1,N+1,0)

print(max_v)