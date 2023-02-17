t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    lst = [list(map(str, input())) for _ in range(n)]
    circular = []
    print(lst)
    # 가로배열
    for i in range(n):
        for j in range(n-m+1):
            if lst[i][j:j+m] == lst[i][j:j+m][::-1]:
                circular.append(''.join(lst[i][j:j+m]))


    # 세로배열
    for i in range(n):
        for j in range(n-m+1):
            sero = []
            for k in range(m):
                sero.append(lst[j+k][i])
            if sero == sero[::-1]:
                circular.append(''.join(sero))

    print(f'#{tc}', *circular)
