for tc in range(1, 11):
    n = int(input())
    lst = [list(map(str, input())) for _ in range(8)]
    print(lst)
    circular = []
    # 가로
    for i in range(8):
        for j in range(8-n+1):
            if lst[i][j:j+n] == lst[i][j:j+n][::-1]:
                circular.append(''.join(lst[i][j:j+n]))
    print(circular)

    # 세로
    for i in range(8):
        for j in range(8-n+1):
            sero = []
            for k in range(n):
                sero.append(lst[j+k][i])
            if sero == sero[::-1]:
                circular.append(''.join(sero))

    print(f'#{tc} {len(circular)}')