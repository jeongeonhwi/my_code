import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    str2 = list(input())
    # print(str1, str2)
    count = 0
    for i in range(len(str2)-len(str1)+1):
        total = []
        for j in range(len(str1)):
            if str2[i+j] == str1[j]:
                total.append(str2[i+j])
        if len(total) == len(str1):
            count += 1
    if count>0:
        count = 1
    print(f'#{tc} {count}')