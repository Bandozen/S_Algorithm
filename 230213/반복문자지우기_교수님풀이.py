t = int(input())

for tc in range(1, t+1):
    row = input()

    # 스택 초기화
    size = 1000
    top = -1
    stack = [0] * size

    # 제일 처음 글자는 비교할 앞 글자가 없을니까 스택에 넣기
    top += 1
    stack[top] = row[0]

    for i in range(1, len(row)):
        if top != -1 and stack[top] == row[i]:
            top -= 1    # == pop
        else:
            top += 1
            stack[top] = row[i] # == push

    print(f'#{tc} {top + 1}')