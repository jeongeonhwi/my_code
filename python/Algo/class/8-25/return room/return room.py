import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        now, room = map(int, input().split())
        if now%2 == 1:
            now +=1
        if room%2 == 1:
            room +=1
        a = []
        if now<=room:
            for i in range(now//2, room//2+1):
                a.append(i)
        else:
            for i in range(room//2, now//2+1):
                a.append(i)
        arr.append(a)
    b = [0]*500
    for i in arr:
        for j in i:
            b[j] += 1
    b.sort()
    print(f'#{tc} {b[-1]}')
