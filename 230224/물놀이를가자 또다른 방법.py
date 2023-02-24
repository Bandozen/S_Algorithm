t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())

    mapp = [list(input()) for _ in range(n)]

    ans = 0

    limit = 2000

    # 오른쪽 아래로 돌면서 min(왼쪽에서 온길, 위쪽에서 온길)
    for r in range(n):
        for c in range(n):
            if mapp[r][c] == "W":
                mapp[r][c] = 0
            else:
                # 위에서 왔을 때 거리
                up = mapp[r-1][c] if r > 0 else limit
                # 왼쪽에서 왔을 때 거리
                left = mapp[r][c-1] if c > 0 else limit
                mapp[r][c] = min(up, left) + 1

    # 왼쪽 위로 돌면서 min(오른쪽에서 온길, 아래쪽에서 온 길)
    for r in range(n-1, -1, -1):
        for c in range(m-1, -1, -1):
            if mapp[r][c] == "W":
                mapp[r][c] = 0
            else:
                # 아래에서 왔을 때 거리
                down = mapp[r+1][c] if r < n - 1 else limit
                # 오른쪽에서 왔을 때 거리
                right = mapp[r][c+1] if c < m - 1 else limit
                mapp[r][c] = min(min(down, right) + 1, mapp[r][c])
                ans += mapp[r][c]

    print('#{} {}'.format(tc, ans))