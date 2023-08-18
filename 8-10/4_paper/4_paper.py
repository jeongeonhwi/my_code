import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nlist = []
    sum = 0
    #규칙을 찾자
    # N//10 이 홀수일 경우 4의 배수로 상승
    if (N//10)%2 != 0:
        if (N//10)//2 != 0:
            for i in range((N//10)//2+1):
                nlist.append(i)
        else:
            nlist.append(0)
        for i in range(len(nlist)):
            sum += 4**i
    # N//10 이 짝수일 경우 5의 배수로 상승
    else:
        if N > 20:
            for i in range(1, (N//10)//2):
                nlist.append(i)
            # print(nlist)
            sum += 3
            for i in nlist:
                sum += 5**i
        else:
            sum += 3
    print(f'#{tc} {sum}')