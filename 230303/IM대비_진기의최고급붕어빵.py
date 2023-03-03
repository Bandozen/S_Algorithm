t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    lst = list(map(int, input().split()))
    cnt = 0
    ans = "Possible"
    for t in sorted(lst):
        cnt += 1
        if cnt > (t//m) * k:
            ans = "Impossible"
            break
    print(f'#{tc} {ans}')