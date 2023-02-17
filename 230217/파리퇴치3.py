dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cross1 = [-1, 1, -1, 1]
cross2 = [-1, -1, 1, 1]

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    c_list = []
    for i in range(n):
        for j in range(n):
            catch1 = 0
            catch2 = 0
            catch1 += arr[i][j]
            catch2 += arr[i][j]
            for k in range(4):
                for k1 in range(1, m):
                    nr = i + dr[k] * k1
                    nc = j + dc[k] * k1
                    if 0 <= nr < n and 0 <= nc < n:
                        catch1 += arr[nr][nc]
                        c_list.append(catch1)
            for o in range(4):
                for p in range(1, m):
                    cr = i + cross1[o] * p
                    cc = j + cross2[o] * p
                    if 0 <= cr < n and 0 <= cc < n:
                        catch2 += arr[cr][cc]
                        c_list.append(catch2)

    maxV = 0
    for i in c_list:
        if maxV < i:
            maxV = i

    print(f'#{tc} {maxV}')