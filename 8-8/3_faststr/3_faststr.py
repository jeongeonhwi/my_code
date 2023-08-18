import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())
    blist = list(A)
    slist = list(B)
    print(blist)
    print(slist)
    total = 0
    i = 0
    # 처음엔 완전 탐색 방법으로 풀었는데 fail이 나왔다.
    # 인덱스를 하나씩 더해가면서 푸니까 예를들어 nnnn이라는 문자열이 나오면
    # 오류가 생겼다. 그래서 while문을 사용해서 해당 문자열을 인식하면
    # 그 문자열의 길이만큼 인덱스를 증가시켜 타이핑 문자의 수를 통제하였다.
    while i < len(blist)-len(slist)+1:
        count = 0
        for j in range(len(slist)):
            if slist[j] == blist[i+j]:
                count += 1
        if count == len(slist):
            total += 1
            i += len(slist)
        else:
            i += 1
    # print(total)
    result = len(blist) - total*len(slist) + total
    print(f'#{tc} {result}')