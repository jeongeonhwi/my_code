import sys
sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')




#원자들의 이동방향 상(0) 하(1) 좌(2) 우(3)
#원자들의 처음 위치 (-1000 <= x,y <= 1000


direction = [(0,0.5), (0,-0.5), (-0.5,0), (0.5,0)]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    year = 0
    check = False
    while True:
        if year >= 4100:
            break
        for i in arr:
            if i != 0:
                x, y, d, k = i
                move_x, move_y = direction[d]
                i[0] += move_x
                i[1] += move_y
        for i in range(len(arr)):
            if arr[i] != 0:

                if arr[i][0] < -1003 and 1003 < arr[i][0]:
                    arr[i] = 0
                elif arr[i][1] < -1003 and 1003 < arr[i][1]:
                    arr[i] = 0
            idx = []
            for j in range(len(arr)):
                if arr[i] != 0 and arr[j] != 0 and i != j:
                    if arr[i][0] == arr[j][0] and arr[i][1] == arr[j][1]:
                        idx.append(i)
                        idx.append(j)

            if len(idx) > 0:
                idx = set(idx)
                idx = list(idx)
                for ii in idx:
                    cnt += arr[ii][3]
                    arr[ii] = 0
        if arr.count(0) >=len(arr)-1:
            break
        if check:
            break
        year += 1
        # print(arr)
    print(f'#{tc} {cnt}')
