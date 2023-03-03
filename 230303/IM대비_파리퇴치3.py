t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for si in range(n):
        for sj in range(n):
            cnt = arr[si][sj]
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                for mul in range(1, m):
                    ni, nj = si+di*mul, sj+dj*mul
                    if 0 <= ni < n and 0 <= nj < n:
                        cnt += arr[ni][nj]
            ans = max(ans, cnt)

            cnt = arr[si][sj]
            for di, dj in ((-1, -1), (1, 1), (1, -1), (1, 1)):
                for mul in range(1, m):
                    ni, nj = si + di * mul, sj + dj * mul
                    if 0 <= ni < n and 0 <= nj < n:
                        cnt += arr[ni][nj]
            ans = max(ans, cnt)

    print(f'#{tc} {ans}')