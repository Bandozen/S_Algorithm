t = int(input())

# 중위탐색 이용!
def inorder(t):
    global num, root, node
    if t <= n:
        inorder(2 * t)
        num += 1
        # 루트노드의 값을 넣어줄때
        if t == 1:
            root = num
        # N//2번노드의 값을 넣어줄때
        elif n // 2 == t:
            node = num
        inorder(2 * t + 1)

for tc in range(1, t+1):
    n = int(input())
    num = 0
    root = 0
    node = 0
    # 1부터시작하니까 중위탐색(1)
    inorder(1)
    print(f'#{tc} {root} {node}')