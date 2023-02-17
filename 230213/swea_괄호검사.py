# {()} 는 제대로 된 짝이지만
# {(}) 는 제대로 된 짝이 아니다.
t = int(input())
for tc in range(1, t+1):
    n = input()
    stack = []
    answer = 1
    for i in n:
        if i == "{":
            stack.append(i)
        if i == "(":
            stack.append(i)
        if i == ")":
            if len(stack) == 0:
                answer = 0
                break

            b = stack.pop()
            if not (b == "(" and i == ")"):
                answer = 0
                break
        if i == "}":
            if len(stack) == 0:
                answer = 0
                break

            b = stack.pop()
            if not (b == "{" and i == "}"):
                answer = 0
                break

    if len(stack) > 0:
        answer = 0

    print(f'#{tc} {answer}')