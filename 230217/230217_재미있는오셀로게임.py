t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    # arr 네방향 0 으로 패딩해서 둘러쌈
    arr = [[0]*(n+2) for _ in range(n+2)]
    # [1] 초기 돌 위치 놓기
    a = n//2
    arr[a][a] = arr[a+1][a+1] = 2
    arr[a+1][a] = arr[a][a+1] = 1

    # [2] 흑돌 백돌 입력받아서 처리
    for _ in range(m):
        si, sj, d = map(int, input().split())
        # 초기에 돌을 놓는다.
        arr[si][sj] = d
        for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
            # 해당 방향으로 뻗어나가면서 처리
            tlst = []
            for mul in range(1, n):
                ni, nj = si + di * mul, sj + dj * mul
                if arr[ni][nj] == 0:    # 빈칸이거나 범위 밖
                    break
                elif arr[ni][nj] != d:  # 다른 돌인 경우 뒤집기 후보에 추가!
                    tlst.append((ni,nj))
                else:                   # 같은 돌 => 후보들을 뒤집고, 종료!
                    while tlst:
                        ti, tj = tlst.pop()
                        arr[ti][tj] = d
                    break
    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f'#{tc} {bcnt} {wcnt}')