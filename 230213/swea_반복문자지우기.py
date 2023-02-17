t = int(input())
for tc in range(1, t+1):
    n = input()
    stack = []
    for i in range(len(n)):
        if len(stack) == 0:
            stack.append(n[i])
        else:
            if stack[-1] == n[i]:
                stack.pop()
            else:
                stack.append(n[i])

    print(f'#{tc} {len(stack)}')