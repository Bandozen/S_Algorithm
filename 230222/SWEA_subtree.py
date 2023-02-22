t = int(input())

def preorder(t):
    global cnt
    if t:
        cnt += 1
        preorder(cleft[t])
        preorder(cright[t])
    return cnt

for tc in range(1, t+1):
    e, n = map(int, input().split())
    tree = list(map(int, input().split()))
    cleft = [0] * (e + 2)
    cright = [0] * (e + 2)
    cnt = 0
    for i in range(e):
        p = tree[i * 2]
        c = tree[i * 2 + 1]
        if cleft[p] == 0:
            cleft[p] = c
        else:
            cright[p] = c

    print(f'#{tc} {preorder(n)}')