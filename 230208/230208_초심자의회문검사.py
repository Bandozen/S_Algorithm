t = int(input())
for tc in range(1, t + 1):
    n = input()
    circular = ''
    for i in n:
        circular = i + circular
    if n == circular:
        answer = 1
    else:
        answer = 0
    print(f'#{tc} {answer}')
