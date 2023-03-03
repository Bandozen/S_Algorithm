t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    answer = 0
    m = n // 2

    # [2] 범위
    s = e = m
    for i in range(n):
        for j in range(s, e+1):
            answer += arr[i][j]
        if i < m:
            s-=1
            e+=1
        else:
            s+=1
            e-=1

    # [1] 규칙성
    # for i in range(n):
    #     for j in range(abs(m-i), n - abs(m-i)):
    #         answer += arr[i][j]

    print(f'#{tc} {answer}')