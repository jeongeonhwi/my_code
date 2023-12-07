'''
이진검색 - 반복문
문제에서 데이터가 정렬되어 있다 라는 조건이 없다면
반드시 정렬을 먼저 수행해야 한다.
첫번째 와일문으로 풀기
두번째 재귀로 풀기
'''

arr = [2, 4, 7, 9, 11, 19, 23]
arr. sort()

def binarySearch(target):
    low = 0
    high = len(arr) -1

    # low >= high 라면 데이터를 못찾은 경우
    while low <= high:
        mid = (low + high) // 2

        # 1. 가운데 값이 정답인 경우
        if arr[mid] == target:
            return mid
        # 2. 가운데 값이 정답보다 작은 경우
        elif arr[mid] < target:
            low = mid+1
        # 3. 가운데 값이 정답보다 큰 경우
        else:
            high = mid -1
    return '해당 데이터는 없습니다.'

# 함수 한번 호출 때마다 low, high 변수가 바뀌어서 사용됨
def binarySearch2(low, high, target):
    # 기저 조건: 언제까지 재귀호출을 반복할 것인가?
    # low > high 데이터를 못찾음
    if low > high:
        return '해당 데이터는 없습니다.'
    mid = (low+high)//2
    # 1. 가운데 값이 정답인 경우
    if arr[mid] == target:
        return mid
    # 2. 가운데 값이 정답보다 작은 경우
    elif arr[mid] < target:
        return binarySearch2(mid+1, high, target)
    # 3. 가운데 값이 정답보다 큰 경우
    else:
        return binarySearch2(low, mid-1, target)


print(f'9 = {binarySearch(9)}')
print(f'4 = {binarySearch(4)}')
print(f'15 = {binarySearch(15)}')

print(f'9 = {binarySearch2(0, len(arr)-1, 9)}')
print(f'4 = {binarySearch2(0, len(arr)-1, 4)}')
print(f'15 = {binarySearch2(0, len(arr)-1, 15)}')