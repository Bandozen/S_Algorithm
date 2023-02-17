def backtracking(row, remain, now_sum):
    global min_sum

    # 0. 가지 치기
    if now_sum > min_sum:
        return

    # 1. 종료 조건
    if row == n and remain == 0:
        if min_sum > now_sum:
            min_sum = now_sum
        return

    # 2. 재귀 호출
    # 현재행 row에서 i번째 열에 있는 숫자를 선택할 수 있는가?
    for i in range(n):
        can_place = True

        # 세로에 선택한 열이 있는지 검사
        for j in range(row):
            if selected[j][i] == 1:
                can_place = False
                break

        # 놓을수 있는지 검사
        if can_place:
            # 놓을수 있으면 현재 위치에 놓고 다음 위치로 이동
            selected[row][i] = 1
            backtracking(row + 1, remain - 1, now_sum + board[row][i])
            # 다시 되돌려놓고 진행 할수 있도록 해준다.
            selected[row][i] = 0


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    # 최소합
    min_sum = 100

    # 보드만들기
    board = [list(map(int, input().split())) for _ in range(n)]
    # 내가 i,j 위치의 칸을 선택했다고 표시
    selected = [[0] * n for _ in range(n)]

    backtracking(0, n, 0)

    print(f"#{tc} {min_sum}")