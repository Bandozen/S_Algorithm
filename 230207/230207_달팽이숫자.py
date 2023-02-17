t = int(input())
# 방향 : 우 => 하 => 좌 => 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(1, t+1):
    n = int(input())
    snail = [[0]*n for _ in range(n)]
    r, c = 0, 0
    d = 0
    for i in range(1, (n*n) + 1):
        snail[r][c] = i
        r += dr[d]
        c += dc[d]
        if r >= n or c >= n or r < 0 or c < 0 or snail[r][c] != 0:
            r -= dr[d]
            c -= dc[d]
            d = (d+1) % 4
            r += dr[d]
            c += dc[d]
    print(f'#{tc}')
    for i in range(len(snail)):
        print(*snail[i])
