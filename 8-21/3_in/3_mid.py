import sys
sys.stdin = open('input.txt')

def inorder(n):
    if n:
        inorder(ch1[n])
        visited.append(n)
        inorder(ch2[n])




T = 10
for tc in range(1, T+1):
    N = int(input())
    pstr = [0]*(N+1)
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    arr = []
    visited = []
    for _ in range(N):
        a = list(input().split())
        arr.append(a)
    # print(arr)
    for i in range(N):
        if len(arr[i]) == 4:
            pstr[int(arr[i][0])] = arr[i][1]
            ch1[int(arr[i][0])] = int(arr[i][2])
            ch2[int(arr[i][0])] = int(arr[i][3])
        elif len(arr[i]) == 3:
            pstr[int(arr[i][0])] = arr[i][1]
            ch1[int(arr[i][0])] = int(arr[i][2])
        else:
            pstr[int(arr[i][0])] = arr[i][1]

    inorder(1)
    print(f'#{tc} ', end='')
    for i in visited:
        print(pstr[i], end='')
    print()