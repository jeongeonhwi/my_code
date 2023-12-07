import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(str(input()))
    i = 0
    # 반복된 문자를 몇번 지우게 될지 모르기 때문에 while문사용하였음
    while i < len(arr) -1:
        if i+1 < len(arr) and arr[i] == arr[i+1]:
            #슬라이스를 사용하여 중복된 두 문자를 제거한뒤 합침
            arr = arr[:i] + arr[i+2:]
            i = 0
        i += 1
    print(f'#{tc} {len(arr)}')