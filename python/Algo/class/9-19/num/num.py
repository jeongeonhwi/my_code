import sys
sys.stdin = open('input.txt', 'r')


def permutation(start, end, value):
    global cnt
    if start == end:
        for i in range(4):
            for j in range(4):
                s = ''
                s += arr[i][j]
                tmpi, tmpj = i, j
                for k in p:
                    ni = tmpi+di[k]
                    nj = tmpj+dj[k]
                    if 0<=ni<4 and 0<=nj<4:
                        s += arr[ni][nj]
                        tmpi, tmpj = ni, nj
                    else:
                        break
                if len(s) >=7:
                    my_set.add(s)
        return
    else:
        for j in range(4):
            p[start] = num[j]
            permutation(start+1, end, value)


di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]
T = int(input())
for tc in range(1, T+1):
    arr = [list(input().split()) for _ in range(4)]
    my_set = set()
    p = [0]*6
    num = [i for i in range(4)]
    permutation(0, 6, 0)
    print(f'#{tc} {len(my_set)}')