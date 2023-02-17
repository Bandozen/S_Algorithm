def get_postfix(string, n):
    postfix = ''
    stack = []

    for i in range(n):
        if "0" <= string[i] <= "9":
            postfix += string[i]
        else:
            stack.append(string[i])

    while stack:
        postfix += stack.pop()

    return postfix

def get_result(postfix):
    stack = []

    for i in postfix:
        if "0" <= i <= "9":
            stack.append(int(i))
        else:
            right = stack.pop()
            left = stack.pop()

            if i == "+":
                result = left + right
                stack.append(result)

    return stack.pop()

for tc in range(1, 11):
    a = int(input())
    string = input()
    n = len(string)
    postfix = get_postfix(string, n)
    print(f'#{tc} {get_result(postfix)}')