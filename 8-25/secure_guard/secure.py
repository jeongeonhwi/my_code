import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_house = 0
    for i in arr:
        max_house += i.count(1)
    k = 1
    while True:
        if k*k+(k-1)*(k-1) > max_house*M:
            k -= 1
            break
        k += 1
    total = 0
    for i in range(N):
        for j in range(N):
            for kk in range(1, k):
                srt_i = i-kk+1
                srt_j = j-kk+1
                print(srt_i, srt_j)
                if 0<=srt_i<N and 0<=srt_j<N:
                    count = 0
                    for ii in range(kk+1):
                        for jj in range(kk+1):
                            ni = srt_i+ii
                            nj = srt_j+jj
                            if 0<=ni<N and 0<=nj<N:
                                if abs(i - ni) + abs(j - nj) <= kk-1:
                                    if arr[ni][nj] == 1:
                                        count += 1
                    if kk*kk+(kk-1)*(kk-1) <= count*M:
                        # print(count)
                        if total <= count:
                            total = count
    print(total)
    print(f'#{tc}')

