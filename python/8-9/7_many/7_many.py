import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    nsize = 0
    total = 0
    for i in range(len(arr)):
        ea = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                ea += 1
                if ea > total:
                    total = ea
                    nsize = arr[i]
                elif ea == total:
                    if nsize < arr[i]:
                        nsize = arr[i]
                        total = ea
    print(f'#{N} {nsize}')