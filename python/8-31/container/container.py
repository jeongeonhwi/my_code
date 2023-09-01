import sys
sys.stdin = open('input.txt', 'r')


# def sunyeol(i, N):
#     if i == N:
#         c = p[:]
#         we_list.append(c)
#         return
#     else:
#         for j in range(N):
#             if used[j] == 0:
#                 p[i] = weight[j]
#                 used[j] = 1
#                 sunyeol(i+1,N)
#                 used[j] = 0



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    weight = list(map(int, input().split()))
    capacity = list(map(int, input().split()))
    # we_list = []
    # p = [0]*N
    # used = [0]*N
    total = 0
    # sunyeol(0, N)
    # for i in we_list:
    #     count = 0
    #     capacheck = [0] * len(capacity)
    #     for ii in i:
    #         for j in range(len(capacity)):
    #             if capacheck[j] == 0:
    #                 if ii <= capacity[j]:
    #                     capacheck[j] = 1
    #                     count += ii
    #                     break
    #     if total <= count:
    #         total = count
    weight.sort(reverse=True)
    capacity.sort(reverse=True)
    count1 = 0
    capacheck = [0] * len(capacity)
    for i in weight:
        for j in range(len(capacity)):
            if i <= capacity[j]:
                if capacheck[j] == 0:
                    count1 += i
                    capacheck[j] = 1
                    break
        if total <= count1:
                total = count1
    print(f'#{tc} {total}')