def backtracking(row, remain):
    global cnt

    # 1. 종료 조건
    if row == n and remain == 0:
        cnt += 1
        return
    # 2. 재귀 호출

    # 현재 행 row에서 i번째 열에 퀸을 놓을 수 있는지?
    for i in range(n):
        can_place = True
        # 세로에 퀸이 있는지 검사
        for j in range(row):
            if board[j][i] == 1:
                can_place = False
                break
        # 대각선에 퀸이 있는지 검사
        for j in range(1, row + 1):
            # 좌상
            if row - j >= 0 and i - j >= 0 and board[row - j][i-j] == 1:
                can_place = False
                break
            # 우상
            if row - j >= 0 and i + j < n and board[row-j][i+j] == 1:
                can_place = False
                break
        # 놓을 수 있는 지 검사
        if can_place:
            # 놓을 수 있으면 현재 위치에 놓고 다음 위치로 이동
            board[row][i] = 1
            backtracking(row + 1, remain - 1)
            # 다시 되돌려놓고 진행할수 있도록 한다.
            board[row][i] = 0


t =int(input())
for tc in range(1, t+1):
    n = int(input())

    # 경우의 수 구하기
    cnt = 0

    # 보드 만들기
    board = [[0] * n for _ in range(n)]
    backtracking(0, n)

    print(f'#{tc} {cnt}')
