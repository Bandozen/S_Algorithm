# 후위순회법
def postorder(t):
    if t:
        postorder(left[t])
        postorder(right[t])
        # 만약에 트리의 부모노드가 연산자일경우
        if tree[t] == "+":
            tree[t] = int(tree[left[t]]) + int(tree[right[t]])
        elif tree[t] == "-":
            tree[t] = int(tree[left[t]]) - int(tree[right[t]])
        elif tree[t] == "*":
            tree[t] = int(tree[left[t]]) * int(tree[right[t]])
        elif tree[t] == "/":
            tree[t] = int(tree[left[t]]) // int(tree[right[t]])


for tc in range(1, 11):
    n = int(input())

    tree = [0] * (n+1)
    left = [0] * (n+1)
    right = [0] * (n+1)

    for _ in range(n):
        a = input().split()
        tree[int(a[0])] = a[1]
        # 사칙연산이니까 자식이 둘 다 존재할 경우 숫자값을 넣어준다.
        if len(a) == 4:
            left[int(a[0])] = int(a[2])
            right[int(a[0])] = int(a[3])
    postorder(1)
    print(f'#{tc} {tree[1]}')
