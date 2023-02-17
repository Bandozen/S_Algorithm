dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, n):
    # 방문 배열 만들기
    visited = [[0] * n for _ in range(n)]
    # 빈 스택
    stack = []

    while True:
        if maze[r][c] == 3:
            return 1

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            # 다음 위치를 갈 수 있는지 검사
            if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] != 1 and not visited[nr][nc]:
                # 다음 위치로 가기전에 현재 위치를 저장
                stack.append((r, c))
                visited[nr][nc] = 1
                r, c = nr, nc
                break
        else:
            # 스택이 비어있지 않다면 하나 꺼내서 되돌아가기
            if stack:
                r, c = stack.pop()
            # 스택이 비어있다면 내가 갈수 있는 길은 모두 다 간것!
            else:
                break

    return 0

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(n)]

    r, c = 0, 0

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                r = i
                c = j
    print(f'#{tc} {dfs(r, c, n)}')