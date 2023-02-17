# 스택 밖에 있을시 우선 순위 (토큰의 우선순위)
icp = {"+" : 1, "-" : 1, "/" : 2, "*" : 2, "(" : 3}
# 스택 안에 있을시 우선 순위
isp = {"+" : 1, "-" : 1, "/" : 2, "*" : 2, "(" : 0}

# infix => 중위표기식
# n => 식의 길이

def get_postfix(infix, n):
    postfix = "" # 결과로 출력할 후위 표기식
    stack = []

    # infix 안에 있는 문자들을 하나씩 떼와서 처리
    for i in range(n):
        # 피연산자인 경우
        if "0" <= infix[i] <= "9":
            # 결과에 출력한다.
            postfix += infix[i]
        # 연산자인 경우
        else:
            # 닫는 괄호가 나오는 경우
            if infix[i] == ")":
                # 여는 괄호가 나올 때까지 pop 해서 결과에 출력
                while stack:
                    char = stack.pop()
                    if char == "(":
                        break
                    postfix += char
            # 다른 연산자가 나오는 경우
            else:
                # 현재 토큰(연산자)의 우선순위보다 stack[top]의 우선순위와
                # 같거나 높으면 계속 pop
                while stack and isp[stack[-1]] >= icp[infix[i]]:
                    postfix += stack.pop()
                # 그게 아니면 push
                stack.append(infix[i])
# 남아있는 연산자를 출력
    while stack:
        postfix += stack.pop()

    return postfix

string = "2+3*4/5"
n = len(string)

print(get_postfix(string, n))

# 후위표기식 결과 계산
def get_result(postfix):
    stack = []

    for c in postfix:
        # 피연산자를 만나면 스택에 넣기
        # 현재 c는 문자열이므로 형변환 해줘야 함
        if "0" <= c <= "9":
            stack.append(int(c))
        # 연산자를 만나면 피연산자를 두개꺼내서 계산
        else:
            # 오른쪽에 있는 숫자가 먼저
            right = stack.pop()
            # 왼쪽이 나중에
            left = stack.pop()

            if c == "+":
                result = left + right
            elif c == "-":
                result = left - right
            elif c == "/":
                result = left / right
            elif c == "*":
                result = left * right

            # 스택에 계산 결과 넣기 (다음 연산을 위해서)
            stack.append(result)

    # 마지막에 남은 결과 하나를 꺼내서 리턴!
    return stack.pop()

string = "2+3*4/5"
n = len(string)

postfix = get_postfix(string, n)

print(get_result(postfix))