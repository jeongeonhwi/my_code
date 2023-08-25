'''
거스름돈 500센트 쿼터 25센트 다임 10센트 니켈 5센트 페니 1세트
동전개수 최소로 센트기준으로 인풋받음

'''

T = int(input())
for _ in range(T):
    cent = int(input())
    print(cent//25, end=' ')
    cent = cent%25
    print(cent//10, end=' ')
    cent = cent%10
    print(cent//5, end=' ')
    cent = cent%5
    print(cent)