import sys
sys.stdin = open('input.txt')

def f(card_num):
    if len(card_num) == 1:
        pass
    # 시작부터 절반
    # if 1 in card_num[s:(0+N-1)//2+1] and 2 in card_num[s:(0+N-1)//2+1] and 3 in card_num[s:(0+N-1)//2+1]:
    #     for i in range(s, (0+N-1)//2+1):
    #         if card_num[i] == 3:
    #             select[i] = 3
    # elif 1 in card_num[s:(0+N-1)//2+1] and 2 in card_num[s:(0+N-1)//2+1]:
    #     for i in range(s, (0 + N - 1) // 2 + 1):
    #         if card_num[i] == 2:
    #             select[i] = 2
    # elif 2 in card_num[s:(0+N-1)//2+1] and 3 in card_num[s:(0+N-1)//2+1]:
    #     for i in range(s, (0 + N - 1) // 2 + 1):
    #         if card_num[i] == 3:
    #             select[i] = 3
    # elif 1 in card_num[s:(0+N-1)//2+1] and 3 in card_num[s:(0+N-1)//2+1]:
    #     for i in range(s, (0 + N - 1) // 2 + 1):
    #         if card_num[i] == 1:
    #             select[i] = 1
    #     card_num[s:(0+N-1)//2+1]
    # card_num[(0+N-1)//2+1:N]




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card_num = list(map(int, input().split()))
    select = [0]*(N+1)
    s = 0
    for i in range(s,(0+N-1)//2+1):
        if 1 in card_num[s:(0+N-1)//2+1] and 2 in card_num[s:(0+N-1)//2+1] and 3 in card_num[s:(0+N-1)//2+1]:
            for i in range(s, (0+N-1)//2+1):
                if card_num[i] == 3:
                    select[i] = 3
                    break
        elif 1 in card_num[s:(0+N-1)//2+1] and 2 in card_num[s:(0+N-1)//2+1]:
            for i in range(s, (0 + N - 1) // 2 + 1):
                if card_num[i] == 2:
                    select[i] = 2
                    break
        elif 2 in card_num[s:(0+N-1)//2+1] and 3 in card_num[s:(0+N-1)//2+1]:
            for i in range(s, (0 + N - 1) // 2 + 1):
                if card_num[i] == 3:
                    select[i] = 3
                    break
        elif 1 in card_num[s:(0+N-1)//2+1] and 3 in card_num[s:(0+N-1)//2+1]:
            for i in range(s, (0 + N - 1) // 2 + 1):
                if card_num[i] == 1:
                    select[i] = 1
                    break
        elif 1 in card_num[s:(0+N-1)//2+1]:
            for i in range(s, (0 + N - 1) // 2 + 1):
                if card_num[i] == 1:
                    select[i] = 1
                    break
        elif 2 in card_num[s:(0+N-1)//2+1]:
            for i in range(s, (0 + N - 1) // 2 + 1):
                if card_num[i] == 2:
                    select[i] = 2
                    break
        elif 3 in card_num[s:(0+N-1)//2+1]:
            for i in range(s, (0 + N - 1) // 2 + 1):
                if card_num[i] == 3:
                    select[i] = 3
                    break

    for i in range((0+N-1)//2+1,N):
        if 1 in card_num[(0+N-1)//2+1:N] and 2 in card_num[(0+N-1)//2+1:N] and 3 in card_num[(0+N-1)//2+1:N]:
            for i in range((0+N-1)//2+1,N):
                if card_num[i] == 3:
                    select[i] = 3
                    break
        elif 1 in card_num[(0+N-1)//2+1:N] and 2 in card_num[(0+N-1)//2+1:N]:
            for i in range((0+N-1)//2+1,N):
                if card_num[i] == 2:
                    select[i] = 2
                    break
        elif 2 in card_num[(0+N-1)//2+1:N] and 3 in card_num[(0+N-1)//2+1:N]:
            for i in range((0+N-1)//2+1,N):
                if card_num[i] == 3:
                    select[i] = 3
                    break
        elif 1 in card_num[(0+N-1)//2+1:N] and 3 in card_num[(0+N-1)//2+1:N]:
            for i in range((0+N-1)//2+1,N):
                if card_num[i] == 1:
                    select[i] = 1
                    break
        elif 1 in card_num[(0+N-1)//2+1:N]:
            for i in range((0+N-1)//2+1,N):
                if card_num[i] == 1:
                    select[i] = 1
                    break
        elif 2 in card_num[(0+N-1)//2+1:N]:
            for i in range((0+N-1)//2+1,N):
                if card_num[i] == 2:
                    select[i] = 2
                    break
        elif 3 in card_num[(0+N-1)//2+1:N]:
            for i in range((0+N-1)//2+1,N):
                if card_num[i] == 3:
                    select[i] = 3
                    break
    for i in range(len(select)):
        if select[i] != 0:
            for j in range(i+1, len(select)):
                if select[j] != 0:
                    if select[i] == 1 and select[j] == 2:
                        select[i] = 0
                    elif select[i] == 1 and select[j] == 3:
                        select[j] = 0
                    elif select[i] == 2 and select[j] == 3:
                        select[i] = 0
                    elif select[i] == 2 and select[j] == 1:
                        select[j] = 0
                    elif select[i] == 3 and select[j] == 1:
                        select[i] = 0
                    elif select[i] == 3 and select[j] == 2:
                        select[j] = 0
                    elif select[i] == 1 and select[j] == 1:
                        select[j] = 0
                    elif select[i] == 2 and select[j] == 2:
                        select[j] = 0
                    elif select[i] == 3 and select[j] == 3:
                        select[j] = 0
    result = 0
    for i in range(len(select)):
        if select[i] != 0:
            result += i
    print(f'#{tc} {result+1}')
