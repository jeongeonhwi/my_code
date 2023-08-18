import sys
sys.stdin = open('input.txt')
# 괄호를 검사하는 함수
def afunction(arr):
    le = '('
    ri = ')'
    le2 = '{'
    ri2 = '}'
    le3 = '['
    ri3 = ']'
    if arr[0] == ri or arr[0] == ri2 or arr[0] == ri3:
        return -1
    lecount = 0
    ricount = 0
    le2count = 0
    ri2count = 0
    le3count = 0
    ri3count = 0
    for i in arr:
        if lecount - ricount < 0 or le2count - ri2count < 0 or le3count - ri3count < 0:
            return -1
        else:
            if i == le:
                lecount += 1
            elif i == ri:
                ricount += 1
            elif i == le2:
                le2count += 1
            elif i == ri2:
                ri2count += 1
            elif i == le3:
                le3count += 1
            elif i == ri3:
                ri3count += 1
    if lecount == ricount and le2count == ri2count and le3count == ri3count:
        return 1
    return -1

T = int(input())
for tc in range(1, T+1):
    arr = str(input())
    result = afunction(arr)
    print(f'#{tc} {result}')