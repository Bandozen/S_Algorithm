# 방향 배열 설정!(우, 하, 대각선 우하)
dr = [1, 1, 1, 0]
dc = [0, 1, -1, 1]
# 이제는 익숙한 유효성검사 함수...
def is_valid(r, c):
    return 0 <= r < n and 0 <= c < n

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    omok = [list(map(str, input())) for _ in range(n)]
    # 정답을 먼저 NO로 설정해주었습니다!
    ans = 'NO'
    for i in range(n):
        for j in range(n):
            # "o"일 경우부터 탐색을 시작했습니다!
            if omok[i][j] == 'o':
                for d in range(4):
                    # 돌이 이미 하나가 놓아져있으므로 1부터 시작!
                    cnt = 1
                    # 현재 위치를 설정 해주었습니다.
                    nr, nc = i, j
                    # 그리고 계속 반복문을 돌려서 5개가 나올때까지 cnt수를 늘려줍니다!
                    while True:
                        nr = nr + dr[d]
                        nc = nc + dc[d]
                        # 만약 유효하지 않다면 그 즉시 반복문 탈출!
                        if not is_valid(nr, nc):
                            break
                        # "o"가 나오지 않는다면 반복문 탈출!
                        if omok[nr][nc] != "o":
                            break
                        # 이 모든게 해당하지 않는다면 오목돌을 카운트 해줍니다.
                        cnt+=1
                    # 중요한 건 여기입니다!
                    # 문제에서 '5개 이상'이라고 했으므로 '>='이걸 써야합니다.
                    # 만약 ==5 라고 했으면 테스트케이스 오류 납니다!
                    if cnt >= 5:
                        ans = 'YES'
                        break

    print(f'#{tc} {ans}')