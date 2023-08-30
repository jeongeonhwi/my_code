'''
부분집합생성방법 : 바이너리 카운팅
아주 중요한 내용!!!!!!!!!!!!!!!!!!!!
A형 1번문제 풀이 방법.
'''

arr = [3,6,7,1,5,4]
N = 6
for i in range(1,1<<N-1):   # //2를 하게 되면 중복되는 값도 없고 앞에 1덕분에 비어있는 집합도 없다.
    group1 = []             # 1<<(N-1) == (1<<N)//2
    group2 = []
    total1 = 0
    total2 = 0
    for j in range(N):
        if i&(1<<j):        # j번 비트가 0이 아니면
            group1.append(arr[j])
            total1 += arr[j]
        else:
            group2.append(arr[j])
            total2 += arr[j]
    r1 = f(group1)
    r2 = f(group2)
    if r1 and r2:
        if min_v > abs(total1-total2):
            pass
