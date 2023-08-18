import sys
sys.stdin = open('input.txt')

def deq():
    global front
    global count
    global count2
    Q[front] = Q[front]//2
    if Q[front] == 0 and count < (pizza_num-size):
        count += 1
        return front
    count2 = 0
    for i in Q:
        if i == 0:
            count2 += 1
    if count2 == size-1:
        return front
    front = (front+1)%size

    return deq()

T = int(input())
for tc in range(1, T+1):
    size, pizza_num = map(int, input().split())
    arr = list(map(int, input().split()))
    Qsize = size
    count = 0
    count2 = 0
    front = 0
    Q = [0]*Qsize
    Q_idx = [0]*Qsize
    for i in range(size):
        Q[i] = arr[i]
        Q_idx[i] = i
    # print(Q)
    # print(Q_idx)
    for i in range(size, pizza_num):
        a = deq()
        arr[a] = 0
        Q[a] = arr[i]
        Q_idx[a] = i
    deq()
    ab = 0
    for i in range(len(Q)):
        if Q[i] != 0:
            ab = i
    print(f'#{tc} {Q_idx[ab]+1}')

    # print(Q_idx[deq()])
    # max_v = 0
    # max_idx = 0
    # for i in range(len(Q)):
    #     if Q[i] > max_v:
    #         max_v = Q[i]
    #         max_idx = i
    # print(Q_idx[max_idx])
    # print(Q)
    # print(arr)
    # print(Q_idx)
    # for i in range(size-1):
    #     a = deq()
    #     arr[a] = 0
    #     Q[a] = arr[size]