#교수님 써머리 백트래킹 재귀사용 순열

arr = [0,1,2,3,4,5,6,7,8,9]
N = len(arr)

def permutation(idx):
    # 종료 조건
    if idx == N:
        print(arr)
        return
    for swap_idx in range(idx, N):    # 바꿀 위치를 반복
        global count
        count += 1
        arr[idx], arr[swap_idx] = arr[swap_idx], arr[idx]
        permutation(idx+1)    # 다음 자리 확인
        arr[swap_idx], arr[idx] = arr[idx], arr[swap_idx]   #원상 복구 (처음 모양에서 또 자리를 바꾸기 때문에 결과를 예측하기 어려워 지고 잘못된 동작을 수행하게 된다.)
        # arr[idx], arr[swap_idx] = arr[swap_idx], arr[idx]

count = 0
permutation(0)
print(count)