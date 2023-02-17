t = 10
n = 100

# 맨 아래에 2라고 쓰인곳부터 출발!
for tc in range(1, t+1):
    int(input())
    ladders = [list(map(int, input().split())) for _ in range(n)]
    # 위치를 내가 직접 움직여야 한다.
    r = 99
    c = -1  # 2라고 표시된 곳부터 올라가기 때문에 리스트 마지막부분을 뜻하는 -1

    # 2라고 표시된 곳 찾기
    for i in range(n):
        if ladders[r][i] == 2:
            c = i

    dr = [0, 0, -1]
    dc = [-1, 1, 0]

    while r > 0:
        # 위치를 한번 옮길 차례가 올때마다 왼쪽, 오른쪽, 위쪽 순서로 검사
        for d in range(3):
            # 다음 위치 계산
            nr = r + dr[d]
            nc = c + dc[d]
            # 다음 위치가 유효한 인덱스인지 검사
            if 0 <= nc < n and 0 <= nr < n and ladders[nr][nc] == 1:
                # 갈 수 있으면 움직이기!
                r = nr
                c = nc
                # 다시 되돌아가는 것을 방지하기 위해서 내가 지난 길을 0으로!
                ladders[r][c] = 0
                break

    print(f'#{tc} {c}')