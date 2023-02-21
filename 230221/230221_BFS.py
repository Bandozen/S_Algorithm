'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
def bfs(v, N):
    visited = [0] * (N + 1)     # visited 생성
    q = [v]                      # 큐 생성
                                # 시작점 인큐
    visited[v] = 1              # 시작점 인큐 표시
    while q:                    # 큐가 비어있지 않으면
        t = q.pop(0)            # 디큐
        print(t, end = ' ')     # t에서 처리할 일
        for v in adjl[t]:       # t에 인접이고 방문한 적 없는 v
            if visited[v] == 0:
                q.append(v)     # v 인큐
                visited[v] = visited[t] + 1  # v 인큐되었음 표시
    print()
    print(visited)

V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    # 방향이 안정해있으므로 두개 다 append 해주어야 함!
    adjl[n1].append(n2)
    adjl[n2].append(n1)

bfs(1, V)