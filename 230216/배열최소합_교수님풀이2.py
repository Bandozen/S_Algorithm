# 현재 i 번째 행에 대해서 j 번째 열을 골라서 합을 만들기
def backtracking(i, now_sum):
    global min_sum

    # 0. 가지치기
    # 현재 내가 알고있는 합이 이전에 구했던 최소합보다 크면 더 진행할 필요가 없다.
    if now_sum > min_sum:
        return

    # 1. 종료조건
    if i == n:
        if now_sum < min_sum:
            min_sum = now_sum
        return

    # 2. 재귀호출
    # 0 ~ n-1 번째 열중에서 이전에 고른적이 없는 j 열을 선택
    for j in range(n):
        # 고른적이 없는지 확인
        if not select[j]:
            select[j] = 1
            # j번째 열을 고르고 합을 구한 다음 다음 행으로 진행
            backtracking(i + 1, now_sum + board[i][j])
            # 다시 돌아와서 이번열을 건너뛰고 다음열로 진행하도록
            select[j] = 0


T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    board = [list(map(int, input().split())) for _ in range(n)]
    # j 번째 열을 골랐는지 체크
    select = [0] * n
    min_sum = 100

    backtracking(0, 0)

    print(f"#{tc} {min_sum}")