t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = [input().split() for _ in range(n)]
    arr1 = [[0]*n for _ in range(n)]
    arr2 = [[0]*n for _ in range(n)]
    arr3 = [[0]*n for _ in range(n)]
    # 90도, 180도, 270도 회전!
    for i in range(n):
        for j in range(n):
            arr1[i][j] = lst[n-1-j][i]
            arr2[i][j] = lst[n-1-i][n-1-j]
            arr3[i][j] = lst[j][n-1-i]

    print(f'#{tc}')
    for a,b,c in zip(arr1, arr2, arr3):
        print(f'{"".join(a)} {"".join(b)} {"".join(c)}')