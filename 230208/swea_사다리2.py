for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    min_ = 100000
    answer = 0
    for i in range(100):
        if arr[0][i] == 1:
            idx = i
            cnt = 0
            for j in range(100):
                if idx > 0 and arr[j][idx - 1] == 1:
                    while idx > 0 and arr[j][idx - 1] > 0:
                        idx -= 1
                        cnt += 1
                elif idx < 99 and arr[j][idx + 1] == 1:
                    while idx < 99 and arr[j][idx + 1] > 0:
                        idx += 1
                        cnt += 1
            if min_ >= cnt:
                min_ = cnt
                answer = i
    print(f'#{tc} {answer}')