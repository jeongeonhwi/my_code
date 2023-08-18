import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    #수열을 이차원리스트로 먼저 구현해주기
    arr = []
    for i in range(1, N+1):
        arr.append([0]*i)
    arr[0][0] = 1
    #for문을 두번 돌면서 파스칼 삼각형 완성하기
    for i in range(1, len(arr)):
        for j in range(len(arr[i])):
            if j == 0:
                arr[i][j] += arr[i-1][0]
            elif j == len(arr[i])-1:
                arr[i][j] += arr[i-1][len(arr[i-1])-1]
            else:
                arr[i][j] += arr[i-1][j-1]
                arr[i][j] += arr[i-1][j]
    print(f'#{tc}')
    for i in range(N):
        print(*arr[i])