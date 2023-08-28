import sys
sys.stdin = open('input.txt')

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


C, R = map(int, input().split())
K = int(input())
num = []
for i in range(1,C*R+1):
    num.append(i)
fake = [[0]*C for _ in range(R)]
top = 0
a = True
i_idx = R
j_idx = 0
while a:
    for k in range(4):
        while True:
            ni = i_idx+di[k]
            nj = j_idx+dj[k]
            if 0<=ni<R and 0<=nj<C:
                if fake[ni][nj] == 0:
                    fake[ni][nj] = num[top]
                    top += 1
                    i_idx = ni
                    j_idx = nj
                    # print(top)
                    # print(fake)
                else:
                    break
            else:
                break
    if top >= len(num):
        a = False

count = 0
# print(fake)
for i in range(R):
    for j in range(C):
        if fake[i][j] == K:
            print(f'{j+1} {R-i}')
            count += 1
if count == 0:
    print('0')