'''
n개에서 r개를 고르는 조합(재귀사용)
만약에 r개가 고정되 있지 않으면 다중 포문으로 해결불가능(재귀사용해야함)

s 선택할 수 있는 구간의 시작
'''

def ncr(n, r, s):
    if r==0:
        print(*comb)
    elif n<r:       # 남은 원소보다 많은 원소를 선택해야 하는 경우
        return
    else:
        for i in range(s, n-r+1):
            comb[r-1] = A[i]       # [n-1] 조합에 포함시키는 경우
            ncr(n-1, r-1, i+1)



A = [1, 2, 3, 4, 5]
N = len(A)
R = 2
comb = [0]*R
ncr(N, R, 0)
