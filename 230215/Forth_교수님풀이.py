t = int(input())

for tc in range(1, t+1):
    exp = input().split()   # 후위표기식

    stack = []

    # 출력할 결과
    result = 0

    for c in exp:
        # 1. c가 피연산자인 경우는 그냥 스택에 추가
        if "0" <= c <= "9":
            stack.append(int(c))
        else:
            # 정상적인 경우 . 을 만났을때 스택에 결과가 하나 남아있어야 한다.
            if c == ".":
                result = stack.pop()
                break
            # 연산자
            # 연산자가 있는데 피연산자의 개수가 부족한 경우
            if len(stack) < 2:
                result = "error"
                break

            # 피연산자의 개수가 충분
            right = stack.pop()
            left = stack.pop()

            if c == "+":
                result = left + right
            elif c == "*":
                result = left * right
            elif c == "/":
                result = left // right
            elif c == '-':
                result = left - right

            # 계산 결과를 다음 연산을 위해 스택에 넣는다.
            stack.append(result)

    # 다 계산을 했는데 피연산자가 남아있다. ==> 잘못된 식
    # (식에서 연산자를 다 사용했는데)
    if stack:
        result = "error"

    print(f'#{tc} {result}')