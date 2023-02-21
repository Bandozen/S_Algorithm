dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n

def bfs(sr, sc):
    visited = [[0] * n for _ in range(n)]
    q = []
    q.append((sr, sc))
    visited[sr][sc] = 1

    while q:
        r, c = q.pop(0)
        if maze[r][c] == 3:
            return visited[r][c] - 2

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

    return 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                print(f'#{tc} {bfs(i, j)}')