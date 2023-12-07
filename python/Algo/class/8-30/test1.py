# key가 있으면 1, 없으면 0을 리턴하는 함수
def f(i, N, key, A):        # i 현재상태, N 목표, key 찾고자 하는 원소
    if i==N:
        return 0            # key가 없는 경우
    elif A[i]==key:
        return 1            # key가 있는 경우
    else:
        return f(i+1, N, key, A)


N = 5
A = [1, 2, 3, 4, 5]
B = [0]*N
key = 10
print(f(0, N, key, A))

a =1
b =2
