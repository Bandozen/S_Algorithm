t = int(input())
for tc in range(1, t+1):
    n = list(map(str, input()))
    m = list(map(str, input()))
    maxV = 0
    for i in n:
        if m.count(i) >= maxV:
            maxV = m.count(i)
    print(f'#{tc} {maxV}')