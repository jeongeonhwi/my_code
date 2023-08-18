import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    building_list = list(map(int, input().split()))

    # 1. 좌, 우 끝은 빌딩이 없다.
    # 2. 현재 빌딩에서 좌, 우로 2칸씩 빌딩의 높이를 찾는다
    # 2-1. 그 중에서 가장 높은 빌딩의 층수를 구한다. (max 값)
    # 2-2. 만약 빌딩이 없는 경우는 그냥 continue 로 넘어간다.
    # 3. 현재 빌딩 높이보다 낮으면 (미만) 이면 조망권이 있는 경우
    # 3-1. 현재 빌딩 높이 - 가장 높은 주변 빌딩 높이 = 조망권이 있는 층의 개수
    # 3-2. 조망권의 층의 개수를 누적한다.
    # 4. 다음 빌딩을 선택한 후 다시 2번 부터 반복한다.

    # for building in building_list:
        # 이렇게 반복하게 되면
        # 좌, 우 2칸씩 확인하는게 번거로울 수 있다. -> enumerate 사용
        # 왜냐면 현재 위치가 어디인지 모른다. (현재위치 == index번호)
    total = 0
    for idx in range(N):  # 빌딩의 개수 : N
        if building_list[idx] == 0:  # 빌딩이 없으면 다음 빌딩
            continue

        current_building = building_list[idx]  # 현재 빌딩
        # 빌딩이 있는 경우 좌 우 2칸씩 확인하자
        delta = [-2, -1, 1, 2]
        max_height = 0   # 가장 높은 빌딩을 저장하는 변수
        for i in range(4):
            # 가장 높은 빌딩인지 확인
            if max_height < building_list[idx + delta[i]]:
                max_height = building_list[idx + delta[i]]

        # 가장 높은 빌딩과 현재 빌딩을 비교해서 조망권이 있는지 확인
        if current_building > max_height:
            total += current_building - max_height

    print(f'#{tc} {total}')