pattern = {'0001101': 0,
           '0011001': 1,
           '0010011': 2,
           '0111101': 3,
           '0100011': 4,
           '0110001': 5,
           '0101111': 6,
           '0111011': 7,
           '0110111': 8,
           '0001011': 9}

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]

    code = ''
    for i in range(n):
        for j in range(m-1, 54, -1):  # 가장 왼쪽으로 치우친 패턴은 0 ~ 55
            if arr[i][j] == '1':    # 암호패턴의 끝 발견
                code = arr[i][j-55:j+1]
                break   # for j 문을 브레이크!!
        if code != '':
            break       # for i 문을 브레이크!!
    # print(code)

    password = [0] * 8      # 8자리 암호
    for i in range(8):
        password[i] = pattern[code[i*7:i*7+7]]
    # print(password)

    check = (password[0] + password[2] + password[4] + password[6]) * \
        3 + password[1] + password[3] + password[5] + password[7]
    cs = sum(password[0:8:2]) * 3 + sum(password[1:8:2])
    ans = 0
    if cs % 10 == 0:        # cs가 10의 배수면
        ans = sum(password)
    print(f'#{tc} {ans}')
