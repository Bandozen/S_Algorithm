t = int(input())
# 우 하 좌 상
# dr[0]
# dc[0]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(1, t+1):
    n = int(input())
    snail = [[0]*n for _ in range(n)]
    # 현재 위치 0, 0 부터 시작
    r, c = 0, 0
    # 방향 : 우 => 하 => 좌 => 상 => 우 ...
    d = 0
    # 1부터 n*n까지 반복
    for i in range(1, n * n + 1):
        # i = 달팽이 안에 들어갈 숫자, 1부터 증가
        # 현재 위치에 1부터 차례대로 넣기
        snail[r][c] = i
        # 다음 위치 계산
        nr = r + dr[d]
        nc = c + dc[d]
        # 다음 위치가 유효한 인덱스 ?? (배열의 범위를 벗어나지 않았고, 다음 위치에 있는 숫자가 0)
        if 0 <= nr < n and 0 <= nc < n and snail[nr][nc] == 0:
            # => 현재 위치를 다음 위치로 변경
            r, c = nr, nc
        # 다음 위치가 유효하지 않다면?
        else:
            # => 방향을 바꾸고 다음 위치를 다시 계산 후 현재 위치를 다음 위치로 변경
            d += 1
            if d == 4:
                d = 0
            # 현재 위치 다시 계산해주기!
            r = r + dr[d]
            c = c + dc[d]

    print(f'#{tc}')
    for i in range(len(snail)):
        print(*snail[i])
