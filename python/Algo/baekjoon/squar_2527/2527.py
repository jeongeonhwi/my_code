import sys
sys.stdin = open('input.txt')

for _ in range(4):
    arr = list(map(int, input().split()))
    a = [arr[0], arr[1], arr[0], arr[3], arr[2], arr[1], arr[2], arr[3]]
    b = [arr[4], arr[5], arr[4], arr[7], arr[6], arr[5], arr[6], arr[7]]

    # 점 판별 조건문
    if arr[0] == arr[6] and arr[1] == arr[7]:
        print('c')
    elif arr[2] == arr[4] and arr[3] == arr[5]:
        print('c')
    elif arr[0] == arr[6] and arr[3] == arr[5]:
        print('c')
    elif arr[2] == arr[4] and arr[1] == arr[7]:
        print('c')
    # 선 판별 조건문
    elif arr[0] == arr[6] and arr[1]<=arr[7]<=arr[3]:
        print('b')
    elif arr[0] == arr[6] and arr[1]<=arr[5]<=arr[3]:
        print('b')
    elif arr[0] == arr[6] and arr[1]>=arr[5] and arr[3]<=arr[7]:
        print('b')
    elif arr[2] == arr[4] and arr[1]<=arr[5]<=arr[3]:
        print('b')
    elif arr[2] == arr[4] and arr[1]<=arr[7]<=arr[3]:
        print('b')
    elif arr[2] == arr[4] and arr[1]>=arr[5] and arr[3]<=arr[7]:
        print('b')
    elif arr[1] == arr[7] and arr[0]<=arr[6]<=arr[2]:
        print('b')
    elif arr[1] == arr[7] and arr[0]<=arr[4]<=arr[2]:
        print('b')
    elif arr[1] == arr[7] and arr[0]>=arr[4] and arr[2]<=arr[6]:
        print('b')
    elif arr[3] == arr[5] and arr[0]<=arr[4]<=arr[2]:
        print('b')
    elif arr[3] == arr[5] and arr[0]<=arr[6]<=arr[2]:
        print('b')
    elif arr[3] == arr[5] and arr[0]>=arr[4] and arr[2]<=arr[6]:
        print('b')
    #공통부분 없음 조건문
    elif arr[1] >= arr[7]:
        print('d')
    elif arr[0] >= arr[6]:
        print('d')
    elif arr[3] <=arr[5]:
        print('d')
    elif arr[2]<=arr[4]:
        print('d')
    else:
        print('a')