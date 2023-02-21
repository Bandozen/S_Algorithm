def bfs(adj_list, v, n):
    visited = [0] * (n+1)
    q = []
    q.append(v)
    visited[v] = 1
    while q:
        p = q.pop(0)
        for i in adj_list[p]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[p] + 1
            if p == G:
                return visited[p] - 1
    return 0

t = int(input())
for tc in range(1, t+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V + 1)]
    for _ in range(E):
        start, to = map(int, input().split())
        adj_list[start].append(to)
        adj_list[to].append(start)
    S, G = map(int, input().split())
    print(f'#{tc} {bfs(adj_list, S, V)}')