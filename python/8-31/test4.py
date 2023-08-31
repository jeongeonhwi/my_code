'''
부분집합의 합 문제 구현하기(비트연산자 말고 재귀함수로 구현)
아래의 10개의 정수 집합에 대한 모든 부분 집합 중 원소의 합이 0이 되는 부분집합을
모두 출력하시오
예 : -1 3 -9 6 7 -6 1 5 4 -2
만약에 부분집합 합이 0이 될경우 return 0 도출
'''

def subset(i, N, s, c):
    if s==0 and c!=0:
        return 1
    elif i==N:
        return 0
    else:
        if subset(i+1, N, s+arr[i], c+1):
            return 1
        if subset(i+1, N, s, c):
            return 1
    return

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
bit = [0]*N
print(subset(0, N, 0, 0))