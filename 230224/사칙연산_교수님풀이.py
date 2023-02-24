def postorder(t):
    # t노드가 숫자인경우
    if node[t].isdigit():
        return int(node[t])
    # t노드가 연산자인경우 후위순회
    else:
        left = postorder(cleft[t])
        right = postorder(cright[t])
        if node[t] == "+":
            node[t] = str(left + right)
        elif node[t] == "*":
            node[t] = str(left * right)
        elif node[t] == "-":
            node[t] = str(left - right)
        elif node[t] == "/":
            node[t] = str(left // right)

        # node[t] 에 저장은 문자열(isdigit)
        # 리턴은 숫자값으로 (사칙연산 계산을 위해)
        return int(node[t])

T = 10
for tc in range(1, T + 1):
    n = int(input())

    # 자식 정보
    cleft = [0] * (n + 1)
    cright = [0] * (n + 1)

    # 인덱스에 저장된 값 또는 연산자
    node = [0] * (n + 1)

    for i in range(n):
        info = input().split()

        idx = int(info[0])

        # 값이 숫자면
        if info[1].isdigit():
            node[idx] = info[1]
        # 값이 연산자면 왼쪽, 오른쪽 자식 정보 저장
        else:
            node[idx] = info[1]
            cleft[idx] = int(info[2])
            cright[idx] = int(info[3])

    print(f"#{tc} {postorder(1)}")