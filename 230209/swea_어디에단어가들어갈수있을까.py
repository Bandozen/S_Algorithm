t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    # 가로
    for i in range(n):
        count = 0
        for j in range(n):
            if puzzle[i][j] == 0:
                if count == k:
                    answer += 1
                count = 0
            else:
                count += 1
        if count == k:
            answer += 1
    # 세로
    for j in range(n):
        count = 0
        for i in range(n):
            if puzzle[i][j] == 0:
                if count == k:
                    answer += 1
                count = 0
            else:
                count += 1
        if count == k:
            answer += 1

    print(f'#{tc} {answer}')
