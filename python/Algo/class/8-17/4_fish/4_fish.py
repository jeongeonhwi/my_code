import sys
sys.stdin = open('input.txt')

# 975, 981
T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    count = 0
    cookie = 0
    people = 0
    arr.sort()
    arr_set = set(arr)
    # print(arr_set)
    customer_dict = {}
    for i in arr_set:
        count2 = 0
        for j in arr:
            if i == j:
                count2 += 1
        customer_dict[i] = count2
    key_list = []
    for i in customer_dict:
        key_list.append(i)
    key_list.sort()
    # print(arr)
    # print(key_list)
    # print(customer_dict[key_list[people]])
    # print(customer_dict)
    result = ''
    while True:
        # print(count)
        if count > 0 and count%M == 0:
            cookie += K
        if people < len(key_list):
            if count == key_list[people]:
                cookie -= customer_dict[key_list[people]]
                people += 1
                # print(people)
                if cookie < 0:
                    result = 'Impossible'
                    break
        if count > key_list[-1]:
            result = 'Possible'
            break
        count += 1
    print(f'#{tc} {result}')
