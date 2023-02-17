for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max1 = 0
    for i in range(100):
        sum1 = 0
        for j in range(100):
            sum1 += arr[i][j]
        if max1 < sum1:
            max1 = sum1

    max2 = 0
    for i in range(100):
        sum2 = 0
        for j in range(100):
            sum2 += arr[j][i]
        if max2 < sum2:
            max2 = sum2

    max3 = 0
    for i in range(100):
        sum3 = 0
        sum3 += arr[i][i]

        if max3 < sum3:
            max3 = sum3

    print(f'#{t} {max(max1, max2, max3)}')