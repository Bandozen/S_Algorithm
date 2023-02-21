def bfs(G, v, n):
    # 방문 배열
    visited = [0] * (n + 1)
    # 큐 생성
    q = []
    # 시작점 큐에 넣은 상태로 반복 시작
    q.append(v)
    visited[v] = 1

    while q:
        t = q.pop(0)    # q에서 하나 꺼내옴!
        print(t)
        # 현재 정점 t에 연결된 모든 정점 i를 탐색
        for i in G[t]:
            # i번 정점을 내가 방문한 적이 없다면
            if not visited[i]:
                # 다음에 방문하기 위해 큐에 넣고
                q.append(i)
                # 방문 처리
                visited[i] = visited[t] + 1

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]

for i in range(E):
    start, to = map(int, input().split())
    G[start].append(to)
    G[to].append(start)

print(G)
bfs(G, 1, V)