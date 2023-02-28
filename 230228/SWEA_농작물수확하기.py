t = int(input())
for tc in range(1, t+1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    profit = 0
    s = n//2
    e = n//2
    for i in range(n):
        for j in range(s, e+1):
            profit += farm[i][j]
        if i < n//2:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    print(f'#{tc} {profit}')
