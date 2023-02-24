p = [[], [0,1,2,3],[0,1],[2,3],[0,3],[1,3],[1,2],[0,2]]
opp = {0:1, 1:0, 2:3, 3:2}
di, dj = [-1,1,0,0],[0,0,-1,1]
def bfs(si, sj, l):
    q = []
    v = [[0] * m for _ in range(n)]     # 가로 세로 다를 때 특히 주의

    q.append((si,sj))
    v[si][sj] = 1
    cnt = 1

    while q:
        ci,cj = q.pop(0)
        if v[ci][cj] == l:
            return cnt

        for dr in p[arr[ci][cj]]:
            ni, nj = ci+di[dr], cj+dj[dr]
            if 0 <= ni <n and 0<= nj < m and v[ni][nj] == 0 and opp[dr] in p[arr[ni][nj]]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                cnt += 1
    # 공간이 좁아서 L일전에 모두 방문
    return cnt



t = int(input())
for tc in range(1, t+1):
    n, m, r, c, l = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans = bfs(r,c,l)
    print(f'#{tc} {ans}')