t = int(input())

for tc in range(1, t+1):
    n, K, a, b = map(int, input().split())
    sky = [input().split() for _ in range(n)]

    star_cnt = 0
    for r in range(n):
        for c in range(n):
            if sky[r][c] == "*":
                star_cnt += 1

    # 2차원 배열 순회
    # k, k-2, k-4, .... 1까지
    min_V = -1
    # k를 반으로 쪼개서 현재위치 기준 - k => 왼쪽
    # 현재위치 기준 + k => 오른쪽, 아래
    # 그러면 범위는? (r-k//2, c-k//2) ~ (r+k//2, c+k//2)
    half = K // 2
    for k in range(half + 1):
        cnt = 0
        for r in range(a - k, a + k + 1):
            for c in range(b - k, b + k + 1):
                # r,c가 2차원 배열 범위 안이면
                if 0<= r < n and 0 <= c < n and sky[r][c] == "*":
                    cnt += 1

        if cnt == star_cnt:
            # 모든 별을 촬영가능하다.
            min_V = half - k
            break
    print(f'#{tc} {min_V}')