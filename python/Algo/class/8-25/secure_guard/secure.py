import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_house = 0
    for i in arr:
        max_house += i.count(1)
    k = 0
    while True:
        if k*k+(k-1)*(k-1) > max_house*M:
            k -= 1
            break
        k += 1
    total = 0
    for i in range(N):
        for j in range(N):
            for kk in range(1, k+1):
                srt_i = i-kk+1
                srt_j = j-kk+1
                count = 0
                for ii in range(kk+kk-1):
                    for jj in range(kk+kk-1):
                        ni = srt_i+ii
                        nj = srt_j+jj
                        if 0<=ni<N and 0<=nj<N:
                            # print(ni, nj)
                            if abs(i - ni) + abs(j - nj) < kk:
                                if arr[ni][nj] == 1:
                                    count += 1
                            # if abs(i - ni) + abs(j - nj) < kk:
                            #     if i == 3 and j == 3 and kk == 4:
                            #         arr[ni][nj] += 1
                            #         count += 1
                # print(count)
                if kk*kk+(kk-1)*(kk-1) <= count*M:
                    # print(count)
                    if total <= count:
                        total = count
    # print(arr)
    print(f'#{tc} {total}')

