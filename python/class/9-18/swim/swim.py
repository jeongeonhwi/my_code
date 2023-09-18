import sys
sys.stdin = open('input.txt', 'r')

def three(cnt, min_sum):
    global min_v
    if cnt >= 12:
        min_v = min(min_v, min_sum)
        return
    else:
        three(cnt+3, min_sum+threemonth)
        three(cnt+1, min_sum+visited[cnt])
        

#1일 1달 3달 1년
T = int(input())
for tc in range(1, T+1):
    day, onemonth, threemonth, year = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [0]*16
    # 1일 정산
    for i in range(12):
        visited[i] = arr[i]*day

    # 1달 정산
    for i in range(12):
        if visited[i] > onemonth:
            visited[i] = onemonth
    min_v = sum(visited)
    p = [0]*16
    three(0, 0)
    ans = min(min_v, year)
    print(f'#{tc} {ans}')