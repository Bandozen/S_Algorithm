t = int(input())

for tc in range(1, t+1):
    n = int(input())
    num_list = list(map(int,input()))

    c = [0] * 10
    for i in num_list:
        c[i] += 1

    for i in range(10):
        if max(c) == c[i]:
            a = i
            b = max(c)

    print(f'#{tc} {a} {b}')