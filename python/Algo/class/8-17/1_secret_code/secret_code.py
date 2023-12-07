import sys
sys.stdin = open('input.txt')

def enq(data):
    global rear
    global front
    if (rear+1)%Qsize == front:
        front = (front+1)%Qsize
    rear = (rear+1)%Qsize
    Q[rear] = data

def deq():
    global front
    global five
    tem = Q[front] -five-1
    Q[front] = Q[front] -five-1
    five = (five+1)%5
    front = (front+1)%Qsize
    return tem


for _ in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    Qsize = 8
    Q = arr[:]
    front = 0
    rear = 0
    five = 0
    while True:
        a = deq()
        if a <= 0:
            break
    # print(Q)
    current_idx = 0
    for i in range(len(Q)):
        if Q[i] <= 0:
            current_idx = i
    Q[current_idx] = 0
    result = Q[current_idx+1:] + Q[:current_idx+1]
    print(f'#{N}', end=' ')
    print(*result)
