import sys
sys.stdin = open('input.txt', 'r')

# 배열, m개의줄, 몇년
N, M, K = map(int, input().split())
# x,y 위치 인덱스2 나무 나이
arr = [list(map(int, input().split())) for _ in range(N)]
ground = [[5]*N for _ in range(N)]
tree = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    tmp = list(map(int, input().split()))
    tree[tmp[0]-1][tmp[1]-1].append(tmp[2])
for _ in range(K):
    # spring, summer
    for i in range(N):
        for j in range(N):
            if not tree[i][j]:
                continue
            tree[i][j].sort(reverse=True)
            cnt = 0
            tmp_tree = []
            while tree[i][j]:
                t = tree[i][j].pop()
                if ground[i][j] < t:
                    cnt += t//2
                    continue
                ground[i][j] -= t
                tmp_tree.append(t+1)
            tree[i][j] = tmp_tree
            ground[i][j] += cnt
    # fall
    for i in range(N):
        for j in range(N):
            for t in tree[i][j]:
                if t%5 == 0:
                    for di,dj in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]:
                        ni,nj = i+di,j+dj
                        if 0<=ni<N and 0<=nj<N:
                            tree[ni][nj].append(1)
    # winter
    for i in range(N):
        for j in range(N):
            ground[i][j] += arr[i][j]
ans = 0
for i in tree:
    for j in i:
        ans += len(j)
print(ans)