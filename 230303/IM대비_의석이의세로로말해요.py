t = int(input())
for tc in range(1, t+1):
    arr = [input() for _ in range(5)]
    ans = ''
    for j in range(15):
        for i in range(5):
            if j < len(arr[i]):
                ans += arr[i][j]
    print(f'#{tc} {ans}')