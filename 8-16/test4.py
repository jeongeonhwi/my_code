#부분집합의 합_재귀2
# s : i-1원소까지 부분집합의 합(포함된 원소의 합)
def f(i, N, s):
    if i==N:
        print(bit, end=' ')
        print(f' : {s}')

        return
    else:
        # 부분집합에 A[i] 포함
        bit[i]=1
        f(i+1,N, s+A[i])
        # 부분집합에 A[i] 빠짐
        bit[i]=0
        f(i+1, N, s)
        return


A = [1, 2, 3]
bit = [0]*3
f(0, 3, 0)