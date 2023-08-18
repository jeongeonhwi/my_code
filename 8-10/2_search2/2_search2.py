import sys
sys.stdin = open('input.txt')

def dfs(start, V, adj_arr):
    #준비단계
    stack = []
    visited = [False]* (V+1)  # 정점 0은 사용하지 않으므로 편의상 +1을 함
    result = []  #방문한 점을 저장하기 위한 list 나중에 join 으로 붙여서 출력할 예정
    #시작
    v = start
    result.append(v)  # 방문 처리
    visited[v] = True

    while True:
        is_find = False
        for idx in range(V+1):
            if adj_arr[v][idx] == 1 and visited[idx] == False:  # 방문 가능 지점 and 방문 했는지 체크
                # 방문하지 않은 경우
                # 이전에 방문한 지점을 stack push
                stack.append(v)
                # 방문처리
                v = idx
                result.append(v)
                # 방문 여부 체크
                visited[v] = True
                is_find = True
                break
        # for 문을 break 없이 다 반복했다면
        # 그것은 이동할 수 있는 곳이 없다는 의미
          # adj_arr == 1 이 없거나
          # visited 가 True 로 된 경우 (이미 방문한 경우)
        # 이전 갈림길로 되돌아 가야한다
          #stack 에서 pop이 필요함
        if is_find == False:
            if len(stack) != 0:
                v = stack.pop()
            else:
                break           # 더 이상 찾을 곳이 없다면 탐색 종료
    return result
T = 1
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = list(map(int, input().split()))
    # 인접 행렬
    adj_arr = [[0]*(V+1) for _ in range(V+1)]  # 0은 사용하지 않기에 인덱싱의 편의를 위해서 +1 해서 생성
    for idx in range(E):
        # print(arr[idx*2], arr[idx*2+1])
        # 연결된 두 점을 찾아서
        x = arr[idx*2]
        y = arr[idx*2+1]
        # 양방향으로 연결된 상태 => 조건에 단방향이라는 이야기가 없음, 그래프 모양에 화살표가 없음
        adj_arr[x][y] = 1  # 1은 연결됨을 표시
        adj_arr[y][x] = 1  # 1은 연결됨을 표시

    result = dfs(1, V, adj_arr)
    print(f'#{tc} {"-".join(map(str, result))}')
