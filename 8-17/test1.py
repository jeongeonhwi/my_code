# Queue front, rear 방식

def enQ(data):
    global rear
    rear += 1
    Q[rear] = data

def deQ():
    global front
    if front == rear:
        print('큐가 비어있음')
        return -1
    else:
        front += 1
        return Q[front]

Qsize = 3
Q = [0] * Qsize
rear = -1
front = -1
enQ(1)
enQ(2)
rear += 1
Q[rear] = 3
print(Q)
while front != rear:
    front += 1
    print(Q[front])

# enQ(4)
# print(deQ())
# print(deQ())
# print(deQ())
# print(deQ())