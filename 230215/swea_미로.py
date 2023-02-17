# 상하좌우 배열
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, n):
    visited = [[0] * n for _ in range(n)]
    stack = []

    while True:
        if arr[r][c] == 3:
            return 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] != 1 and not visited[nr][nc]:
                stack.append((r, c))
                visited[nr][nc] = 1
                r, c = nr, nc
                break
        else:
            if stack:
                r, c = stack.pop()
            else:
                return 0


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr=[]
    for _ in range(n):
        num_list = list(map(int, input()))
        arr.append(num_list)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                print(f'#{tc} {dfs(i, j, n)}')