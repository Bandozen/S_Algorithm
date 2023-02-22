def inorder(t):
    global tree, string
    if t <= n:
        inorder(t * 2)
        for i in range(len(tree)):
            if t == int(tree[i][0]):
                string += tree[i][1]
        inorder(2 * t + 1)

for tc in range(1, 11):
    n = int(input())
    tree = [list(map(str, input().split()))[:2] for _ in range(n)]
    string = ''
    inorder(1)
    print(f'#{tc} {string}')