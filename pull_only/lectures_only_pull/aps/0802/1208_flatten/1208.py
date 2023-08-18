import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    dump_limit = int(input())
    box_list = list(map(int, input().split()))

    # 1회 덤프
    # 최고값과 최저값을 찾고
    # 최고값은 -1, 최저값은 +1을 한다.
    # 덤프를 총 limit 횟수 만큼 한다.
    # 모든 덤프가 끝나면
    # 최대값과 최소값의 차를 반환한다.
    # for 값, 인덱스 in
    # 값을 돌리게 되면 어떤 위치에 있는 값이 최고값인지 알수 없다.
    # 위치를 알 수 없으면 그 자리에 있는 최고 혹은 최소 값을 수정할수가 없다는 의미
    # 즉, dump를 할 수 없게 됨.
    # 위치가 필요하므로 결국은 인덱스를 이용하여 반복하는 것이 유리!

    for dump in range(dump_limit):
        # 비교 대상의 값을 초기값으로 가져간다.
        min_value = box_list[0]
        min_idx = 0
        max_value = box_list[0]
        max_idx = 0
        for idx in range(1, len(box_list)):  # index 1부터 비교 (초기 값이 0번 인덱스)
            if min_value > box_list[idx]:
                min_value = box_list[idx]
                min_idx = idx

            if max_value < box_list[idx]:
                max_value = box_list[idx]
                max_idx = idx

        # 최대값과 최소값의 차이가 1 이하이면 평탄화가 완료!
        if max_value - min_value <= 1:
            break

        # 최대값에서 1을 빼고, 최소 값에 1을 더한다.
        box_list[max_idx] -= 1
        box_list[min_idx] += 1
        ####### 1회 덤프

    # 모든 덤프가 끝나면 최대값과 최소값을 찾는다. 그리고 뺀다.
    max_value = box_list[0]
    min_value = box_list[0]
    for box in box_list:
        if max_value < box:
            max_value = box
        if min_value > box:
            min_value = box

    # 최대, 최소 값을 찾으면 그 차이를 저장
    result = max_value - min_value

    print(f'#{tc} {result}')