#너비 우선탐색 길찾기

'''
연결되 있는 두개의 정점 사이의 간선을 순서대로 나열해 놓은 것이다. 모든 정점을
 너비우선탐색하여 출력하시오. 시작 정점을 1로 시작하시오.
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

1016010001
'''

def bfs(s, V):  # 시작정점 s, 마지막 정점 V
    # visited 생성
    visited = [0] * (V+1)
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append(s)
    # 시작점 방문표시
    visited[s] = 1
    # 큐에 정점이 남아있으면 front != rear
    while q:
        t = q.pop(0)
        print(t)    # 방문한 정점에서 할일
        for w in adj_l[t]:            # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w]==0:               # w 인큐, 인큐되었음을 표시
                q.append(w)
                visited[w] = visited[t] +1



def bfs2(s, V):  # 시작정점 s, 마지막 정점 V
    # visited 생성
    visited = [0] * (V+1)
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append(s)
    # 시작점 방문표시
    visited[s] = 1
    # 큐에 정점이 남아있으면 front != rear
    while q:
        t = q.pop(0)
        print(t)    # 방문한 정점에서 할일
        for w in range(1, V+1):            # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if adj_m[t][w]==1 and visited[w]==0:               # w 인큐, 인큐되었음을 표시
                q.append(w)
                visited[w] = visited[t] +1






V, E = map(int, input().split())
arr = list(map(int, input().split()))
#인접리스트-----------------------
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)
# 여기까지 인접리스트 -------------------
# bfs(1, 7)

# 인접행렬방식----------------------
adj_m = [[0]*(V+1) for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_m[v1][v2] = 1
    adj_m[v2][v1] = 1  # 방향이 없는 경우
# 여기까지가 인접행렬방식--------------
bfs2(2, V)