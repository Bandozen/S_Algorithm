T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    min_ = sum(arr[:M])
    max_ = 0
    for i in range(N - M + 1):
        sum_ = sum(arr[i:i+M])
        if sum_ < min_:
            min_ = sum_
        if sum_ > max_:
            max_ = sum_
    answer = max_ - min_
    print(f'#{tc} {answer}')
