t = int(input())
for tc in range(1, t+1):
    n = int(input())
    cnts = [0]*200
    for _ in range(n):
        s, e = map(int, input().split())
        if s > e:
            s, e = e, s
        for i in range((s-1)//2, (e-1)//2 + 1):
            cnts[i] += 1

    ans = max(cnts)
    print(f'#{tc} {ans}')