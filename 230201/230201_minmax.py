T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    min_ = 1000000
    max_ = 0
    answer = 0
    for i in range(N):
        if max_ <= arr[i]:
            max_ = arr[i]
    for j in range(N):
        if min_ >= arr[j]:
            min_ = arr[j]
    answer = max_ - min_
    print(f'#{tc} {answer}')