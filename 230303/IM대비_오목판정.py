def solve(arr):
    for si in range(1, n+1):
        for sj in range(1, n+1):
            for di, dj in ((-1, 1), (0, 1), (1, 1), (1, 0)):
                for mul in range(5):
                    ni, nj = si + di*mul, sj + dj*mul
                    if arr[ni][nj] != 'o':
                        break
                else:
                    return 'YES'

    return 'NO'

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = ['.'*(n+2)] + ['.' + input() + '.' for _ in range(n)] + ['.'*(n+2)]

    ans = solve(arr)
    print(f'#{tc} {ans}')