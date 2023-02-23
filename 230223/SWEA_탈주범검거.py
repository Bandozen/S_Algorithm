from pprint import pprint
# 터널 구조물
dic = {1 : [(-1, 0), (1, 0), (0, -1), (0, 1)],
       2 : [(-1, 0), (1, 0)],
       3 : [(0, -1), (0, 1)],
       4 : [(-1, 0), (0, 1)],
       5 : [(1, 0), (0, 1)],
       6 : [(1, 0), (0, -1)],
       7 : [(-1, 0), (0, -1)]}

def is_valid(r, c):
    return 0 <= r < n and 0 <= c < m

t = int(input())
for tc in range(1, t+1):
    n, m, r, c, l = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1
    q = [(r, c)]
    cnt = 1
    while q:
        r, c = q.pop(0)
        for a, b in dic[tunnel[r][c]]:
            nr = r + a
            nc = c + b
            if is_valid(nr, nc) and tunnel[nr][nc] != 0 and (-a, -b) in dic[tunnel[r][c]] and not visited[nr][nc]:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                if visited[nr][nc] <= l:
                    break
                else:
                    cnt+=1

    print(f'#{tc} {cnt}')
