import sys
sys.stdin = open('input.txt', 'r')

#오른쪽 위, 오른쪽 아래, 왼쪽 위, 왼쪽 아래
di = [-1, 1, -1, 1]
dj = [1, 1, -1, -1]


w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
fake = [[0]*w for _ in range(h)]
i_idx = h-q
j_idx = p
print(q, p)
print(i_idx, j_idx)
count = 0
k_idx = 0
while True:
    if count == t:
        break
    ni = i_idx+di[k_idx%4]
    nj = j_idx+dj[k_idx%4]
    if 0<=ni<h and 0<=nj<w:
        i_idx = ni
        j_idx = nj
        count += 1
        print(i_idx, j_idx)
    else:
        k_idx += 1
        print(k_idx)
print(count)
print(j_idx, h-i_idx)