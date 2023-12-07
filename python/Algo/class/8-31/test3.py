'''
부분집합의 합 문제 구현하기(비트연산자 말고 재귀함수로 구현)
아래의 10개의 정수 집합에 대한 모든 부분 집합 중 원소의 합이 0이 되는 부분집합을
모두 출력하시오
예 : -1 3 -9 6 7 -6 1 5 4 -2

'''

def subset(i, N):
    if i==N:
        s = 0
        for j in range(N):
            if bit[j]:
                s += arr[j]
        if s==0:
            for j in range(N):
                if bit[j]:
                    print(arr[j], end = ' ')
            print()
    else:
        bit[i] = 1
        subset(i+1, N)
        bit[i] = 0
        subset(i+1, N)
    return

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
bit = [0]*N
subset(0, N)