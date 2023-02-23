t = int(input())
for tc in range(1, t+1):
    n, m, l = map(int, input().split())
    tree = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        tree[a] = b
    for i in range(n, 0, -1):
        tree[i//2] += tree[i]

    print(f'#{tc} {tree[l]}')