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
    print(arr)
    total = 1
    while arr:
        count = 0
        # print(arr)
        b = arr.pop()
        if arr:
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    for k in range(len(b)):
                        if arr[i][j] == b[k]:
                            count += 1
                            break
                    if count > 0:
                        break
                if count > 0:
                    break
            if count > 0:
                total += 1
    print(f'#{tc} {total}')
