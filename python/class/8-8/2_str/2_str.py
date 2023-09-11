import sys
sys.stdin = open('input.txt')
#딕셔너리로 풀기 도전
T = int(input())
for tc in range(1, T+1):
    str1 = list(input())
    arr = list(input())
    #세트로 중복문자 제거
    s_str1 = set(str1)
    #다시 리스트로 바꾸고
    l_str1 = list(s_str1)
    d_str1 = {}
    #딕셔너리에 리스트의 인덱스+1을 벨류로 넣음
    for i in range(1, len(l_str1)+1):
        d_str1[l_str1[i-1]] = i
    # 딕셔너리로 문제풀기 실패 리스트 다시만듬
    totallist = []
    for i in arr:
        totallist.append(d_str1.get(i))
    # 리스트 요소가 각 리스트를 순회하면서 카운트함
    result = 0
    for i in range(1, len(l_str1) + 1):
        # print(i)
        count = 0
        for j in range(len(totallist)):
            if totallist[j] == i:
                count += 1
        if count > result:
            result = count
    print(f'#{tc} {result}')