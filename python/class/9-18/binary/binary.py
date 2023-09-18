import sys
sys.stdin = open('input.txt', 'r')


def binary(find):
    global cnt
    low = 0
    high = N-1
    check = 5
    while low <= high:
        mid = (low + high) // 2
        if nlist[mid] == find:
            cnt += 1
            return
        elif nlist[mid] < find:
            low = mid + 1
            if not check:
                return
            else:
                check = 0
        else:
            high = mid - 1
            if check==1:
                return
            else:
                check = 1

    return



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nlist = list(map(int, input().split()))
    mlist = list(map(int, input().split()))
    nlist.sort()
    cnt = 0
    for i in mlist:
        if i in nlist:
            binary(i)
    print(f'#{tc} {cnt}')
