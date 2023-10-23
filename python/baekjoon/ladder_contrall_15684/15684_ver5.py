import sys
sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline



from itertools import combinations
N, M, H = map(int, input().split())
arr = [[0]*(N) for _ in range(H)]
abset = set()
for _ in range(M):
    a,b = map(int, input().split())
    arr[a-1][b-1] = 1
    arr[a-1][b] = -1
    abset.add((a-1,b-1))
num = []
for i in range(H):
    for j in range(N-1):
        if j >= 1:
            if arr[i][j] != 0 or arr[i][j-1] != 0 or arr[i][j+1] !=0:
                continue
        else:
            if arr[i][j] != 0 or arr[i][j+1] !=0:
                continue
        num.append((i,j))
ans = -1
pcheck = False
for m in range(4):
    if m != 0:
        combi = combinations(num,m)
        for com in combi:
            check = 0
            for p in com:
                double = set(com)|abset
                if (p[0], p[1] + 1) in double:
                    pcheck = True
                    break
                elif (p[0], p[1] - 1) in double:
                    pcheck = True
                    break
            if pcheck:
                pcheck = False
                continue

            for p in com:
                arr[p[0]][p[1]] = 1
                arr[p[0]][p[1]+1] = -1
            # for ar in arr:
            #     print(ar)
            # print()
            jcheck = False
            for j in range(N):
                if jcheck:
                    jcheck = False
                    break
                jp = j
                for i in range(H):
                    jp+=arr[i][jp]
                if jp != j:
                    jcheck = True
                    break
                else:
                    check+=1
            if check == N:
                ans = m
                break
            for p in com:
                arr[p[0]][p[1]] = 0
                arr[p[0]][p[1] + 1] = 0
        if ans != -1:
            break
    else:
        check = 0
        jcheck = False
        for j in range(N):
            if jcheck:
                jcheck = False
                break
            jp = j
            for i in range(H):
                jp += arr[i][jp]
            if jp != j:
                jcheck = True
                break
            else:
                check += 1
        if check == N:
            ans = m
            break
    if ans != -1:
        break
print(ans)

