t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [[""] * 10 for _ in range(10)]
    for nc in range(n):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if color == 1:
                    arr[i][j] += "R"
                else:
                    arr[i][j] += "B"
    cnt = 0
    for i in range(10):
        for j in range(10):
            if "R" in arr[i][j] and "B" in arr[i][j]:
                cnt += 1

    print(f'#{tc} {cnt}')