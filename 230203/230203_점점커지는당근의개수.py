t = int(input())
for tc in range(1, t+1):
    n = int(input())
    c = list(map(int, input().split()))
    cnt = 1
    ans = 1
    for i in range(n-1):
        if c[i+1] - c[i] != 1:
            cnt = 1
        else:
            cnt += 1
            if cnt > ans:
                ans = cnt

    print(f'#{tc} {ans}')