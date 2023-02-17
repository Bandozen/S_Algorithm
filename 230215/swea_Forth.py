def get_result(arr):
    stack = []
    for c in arr:
        if "0" <= c <= "9":
            stack.append(int(c))
        elif c == ".":
            if len(stack) != 1:
                return "error"
            else:
                return stack.pop()
        else:
            if len(stack) == 1:
                return "error"
            else:
                right = stack.pop()
                left = stack.pop()

                if c == "+":
                    result = left + right
                elif c == "-":
                    result = left - right
                elif c == "/":
                    result = left // right
                elif c == "*":
                    result = left * right

                stack.append(result)


t = int(input())
for tc in range(1, t + 1):
    arr = map(str, input().split())
    print(f'#{tc} {get_result(arr)}')
