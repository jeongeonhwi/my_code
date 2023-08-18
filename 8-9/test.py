T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input()))
    result = 0
    if (arr[4]*10 + arr[5]) > 12:
        result += 1
    else:
        if arr[6]*10 + arr[7] < 1 or arr[6]*10 + arr[7] > 31:
            result += 1
        elif (arr[4]*10 + arr[5]) == 2 and arr[6]*10 + arr[7] > 28:
            result += 1
        elif (arr[4]*10 + arr[5]) == 2 and arr[6]*10 + arr[7] > 30:
            result += 1