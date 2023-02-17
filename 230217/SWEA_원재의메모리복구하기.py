t = int(input())
for tc in range(1, t + 1):
    target = list(input())
    n = len(target)
    bit = ["0"] * n

    cnt = 0

    for i in range(n):
        if target[i] != bit[i]:
            cnt += 1
            for j in range(i, n):
                bit[j] = target[i]

        if target == bit:
            break

    print(f'#{tc} {cnt}')