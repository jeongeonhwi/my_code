# 선형형태의 큐

def enq(data):
    global rear
    global front
    if (rear+1)%cQsize==front:
        front = (front+1)%cQsize
    rear = (rear+1)%cQsize
    cQ[rear] = data


def deq():
    global front
    tmp = cQ[front]
    front = (front+1)%cQsize
    return tmp


cQsize = 4
cQ = [0]*cQsize
front = 0
rear = 0

enq(1)
enq(2)
enq(3)
enq(4)
print(deq())
print(deq())
print(deq())
print(deq())