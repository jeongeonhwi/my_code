#부분집합의 합_연습문제 t:찾으려는 합
def f(i, N, s, t):
    global count
    count += 1
    #
    if s == t:
        print(bit)
        return
    # 남은 원소가 없는경우
    elif i == N:
        return
    elif s > t:
        return
    else:
        # 부분집합에 A[i] 포함
        bit[i] = 1
        f(i + 1, N, s + A[i], t)
        # 부분집합에 A[i] 빠짐
        bit[i] = 0
        f(i + 1, N, s, t)
        return

# 1부터 10까지 원소인 집합, 부분집합의 합이 10인 경우는?
N = 10
A = [i for i in range(1, N+1)]
bit = [0] * N
count = 0
f(0, N, 0, 55)
print(count)