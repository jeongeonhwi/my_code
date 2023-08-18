import sys
sys.stdin = open('input.txt')

swich_num = int(input())
arr = list(map(int, input().split()))
people = int(input())
for _ in range(people):
    gen, style = map(int, input().split())
    #남학생일 경우
    if gen == 1:
        for i in range(swich_num):
            if (i+1)%style == 0:
                if arr[i] == 1:
                    arr[i] = 0
                else:
                    arr[i] =1
    #여학생일 경우
    else:
        if arr[style-1] == 1:
            arr[style-1] = 0
        else:
            arr[style-1] = 1
        for i in range(1, swich_num):
            if 0<= style-1-i and style-1+i < swich_num:
                if arr[style-1-i] == arr[style-1+i]:
                    if arr[style-1-i] == 1:
                        arr[style - 1 - i] = 0
                        arr[style -1+i] = 0
                    else:
                        arr[style -1 -i] = 1
                        arr[style-1+i] = 1
                else:
                    break
for i in range(0, len(arr), 20):
    print(*arr[i:20+i])
