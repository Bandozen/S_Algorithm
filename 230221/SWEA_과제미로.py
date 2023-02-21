dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(r, c):
    return 0 <= r < 16 and 0 <= c < 16

def bfs(sr, sc):
    visited = [[0] * 16 for _ in range(16)]
    q = []
    q.append((sr, sc))
    visited[sr][sc] = 1
    while q:
        r, c = q.pop(0)
        if maze[r][c] == 3:
            return 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and maze[nr][nc] != 1 and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = 1

    return 0

for tc in range(1, 11):
    t = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                print(f'#{t} {bfs(i, j)}')