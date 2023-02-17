t = int(input())

for tc in range(1, t+1):
    a = input()
    b = input()
    answer = 0
    if a in b:
        answer = 1
    else:
        answer = 0
    print(f'#{tc} {answer}')