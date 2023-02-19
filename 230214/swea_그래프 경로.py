def dfs(s, g):
    visited = [0] * (v + 1)
    stack = []
    i = s
    visited[i] = 1

    while True:
        if i == g:
            return 1
        else:
            for w in adj_list[i]:
                if visited[w] == 0:
                    stack.append(w)
                    i = w
                    visited[w] = 1
                    break
            else:
                if stack:
                    i = stack.pop()
                else:
                    return 0


t = int(input())
for tc in range(1, t+1):
    v, e = map(int, input().split())
    adj_list = [[] for _ in range(v + 1)]
    for i in range(e):
        start, to = map(int, input().split())
        adj_list[start].append(to)
    s, g = map(int, input().split())
    print(f'#{tc}', dfs(s, g))
