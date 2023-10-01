'''
문제스타일 : 순열과 구현을 사용하는 문제
접근1. 회전연산의 순서에 따라 값이 다르기 때문에 회전연산을 순열시킨다.
접근2. 순열시킨 배열을 사용하여 회전을 구현한다.
'''



import sys
sys.stdin = open('input.txt', 'r')

import copy
# 순열을 만들어 주는 함수 생성
def permutation(start, end):
    if start == end:
        c = p[:]
        num_list.append(c)
        return
    for j in range(K):
        if used[j] == 0:
            p[start] = num[j]
            used[j] = 1
            permutation(start+1,end)
            used[j] = 0


# 오른쪽, 아래, 왼쪽, 위
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
N,M,K = map(int, input().split())
arr2 = [list(map(int, input().split())) for _ in range(N)]
num = [list(map(int, input().split())) for _ in range(K)]
used = [0]*K
p = [0]*K
num_list = []
permutation(0,K)
min_v = float('inf')
# 순열을 꺼내주는 포문
for n in num_list:
    arr = copy.deepcopy(arr2)
	# 순열의 각 순서를 꺼내주는 포문
    for u in n:
		# 생각해보니까 연산순서 2번인덱스 만큼만 회전하면 되기때문에
		# 2번인덱스만큼 포문
        for k in range(u[2]):
			# 회전의 왼쪽 위 점 생성
            si,sj = u[0]-u[2]-1+k,u[1]-u[2]-1+k
			# 회전의 오른쪽 아래 점 생성
            ei,ej = u[0]+u[2]-1-k,u[1]+u[2]-1-k
            d = 0
			# now i, now j 의 약자로 현재 위치를 표시해줌
            ni, nj = si+di[d], sj+dj[d]
			# 내 앞의 위치를 현재 위치로 덮기때문에 그 값을 저장해주는
			# 임시변수
            tmp = arr[si][sj]
            while True:
			    # 만약 현재위치가 시작점에 도달하면 끝내주는 조건문
                if ni==si and nj==sj:
                    arr[ni][nj] = tmp
                    break
				# 구현시작
                if si<=ni<=ei and sj<=nj<=ej:
										# 다음값을 없애기 전에 변수에 저장
                    tmp2 = arr[ni][nj]
										# 다음위치를 현재값으로 덮음
                    arr[ni][nj] = tmp
										# 현재값을 다음값으로 저장
                    tmp = tmp2
										# 현재위치 이동
                    ni+=di[d]
                    nj+=dj[d]
                else:
					# 잘못간 위치를 복구시키고
                    ni-=di[d]
                    nj-=dj[d]
					# 방향 조절하고
                    d+=1
					# 다음 위치로 이동^^
                    ni+=di[d]
                    nj+=dj[d]
	# 배열 A 구하기
    for i in arr:
        min_v = min(min_v, sum(i))
print(min_v)