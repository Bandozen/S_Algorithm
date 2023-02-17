for tc in range(1, 11):
    dump = int(input())
    height = list(map(int, input().split()))

    cnt = [0] * 101
    for i in height:
        cnt[i] += 1


    min_ = 101
    max_ = 0
    for box in height:
        if box < min_:
            min_ = box
        if box > max_:
            max_ = box

    # 현재 덤프 횟수
    n = 0
    while n < dump:
        cnt[max_] -= 1
        cnt[max_-1] += 1
        cnt[min_] -= 1
        cnt[min_+1] += 1

        if cnt[max_] == 0:
            max_ -= 1
        if cnt[min_] == 0:
            min_ += 1

        n += 1

    result = max_ - min_

    print(f'#{tc} {result}')