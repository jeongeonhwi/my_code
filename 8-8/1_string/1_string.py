# import sys
# sys.stdin = open('input.txt')

for _ in range(10):
    N = int(input())
    list1 = list(input())
    arr = list(input())
    #고지식한방법
    count = 0
    for i in range(len(arr)-len(list1)+1):
        total = 0
        for j in range(len(list1)):
            if list1[j] == arr[i+j]:
                total += 1
        if total == len(list1):
            count += 1
    print(f'#{N} {count}')
