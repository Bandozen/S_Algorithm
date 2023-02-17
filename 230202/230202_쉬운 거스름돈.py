T = int(input())

for tc in range(1, T+1):
    money = int(input())
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    c = [0] * 8

    for i in range(len(money_list)):
        c[i] = int(money / money_list[i])
        money = money % money_list[i]

    result = ' '.join(map(str, c))
    print(f'#{tc}')
    print(f'{result}')