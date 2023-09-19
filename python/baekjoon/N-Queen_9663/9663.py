import sys
sys.stdout = open('output.txt', 'w')


def find_position(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                return (i,j)



di = [1, -1, 0, 0, 1, -1, -1, 1]
dj = [0, 0, 1, -1, 1, 1, -1, -1]

N = int(input())
arr = [[1]*N for _ in range(N)]
for _ in range(N):
    for ii in arr:
        print(ii)
    print()
    i, j = find_position(arr)
    arr[i][j] = 0
    for k in range(8):
        cnt = 1
        ni, nj = i + di[k]*cnt, j + dj[k]*cnt
        while True:
            if 0<=i + di[k]*cnt<N and 0<=j + dj[k]*cnt<N:
                arr[i + di[k]*cnt][j + dj[k]*cnt] = 0
                cnt += 1
            else:
                break

print(arr)