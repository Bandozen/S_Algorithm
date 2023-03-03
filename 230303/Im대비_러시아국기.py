t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]

    mx = 0
    for i in range(n-2):
        for j in range(i+1, n-1):
            cnt = 0
            for s in range(i+1):
                cnt += arr[s].count('W')
            for s in range(i+1, j+1):
                cnt += arr[s].count('B')
            for s in range(j+1, n):
                cnt += arr[s].count('R')
            mx = max(mx, cnt)
    print(f'#{tc} {n*m - mx}')