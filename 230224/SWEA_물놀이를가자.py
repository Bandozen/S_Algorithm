from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid(r, c):
    return 0 <= r < n and 0 <= c < m

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    water = deque()

    mapp = [[-1] * m for _ in range(n)]

    # 입력을 받으면서 w처리(나중에 또 n*m만큼 돌면서 w를 확인x)
    # 물을 만날때마다 bfs를 돌리는게 아니라
    # 모든 물 위치를 큐에 넣어놓고 한번만 bfs를 돌리면 된다.
    for r in range(n):
        row = list(input())
        for c in range(m):
            if row[c] == "W":
                # 물이 있는 곳은 거리가 0
                water.append((r, c))
                mapp[r][c] = 0

    sum_d = 0
    while water:
        r, c = water.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and mapp[nr][nc] == -1:
                water.append((nr, nc))
                mapp[nr][nc] = mapp[r][c] + 1
                # 여기서 합을 처리 (나중에 n*m만큼 순회 X)
                sum_d += mapp[nr][nc]

    print(f'#{tc} {sum_d}')
    print('#{} {}'.format(tc, sum_d))