t = int(input())

for tc in range(1, t+1):
    n, m, = map(int, input().split())

    paper = [[0] * n for _ in range(n)]

    # 도장이 찍힌 곳의 개수
    cnt = 0

    for i in range(m):
        r1, c1, w, h = map(int, input().split())

        for r in range(r1, r1 + h):
            for c in range(c1, c1 + w):
                if paper[r][c] == 0:
                    paper[r][c] = 1
                    cnt+=1

    print(f'#{tc} {cnt}')