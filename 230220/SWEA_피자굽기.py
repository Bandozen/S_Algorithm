t = int(input())

for tc in range(1, t+1):
    # n은 오븐크기, m은 피자 개수
    n, m = map(int, input().split())

    # 우리가 구워야 할 피자들의 치즈 정보
    cheese = list(map(int, input().split()))

    # 다음에 꺼내올 피자의 번호
    next_i = 0

    # 오븐
    oven = [0] * 1000
    ofront = orear = -1

    # 오븐에 차례대로 피자를 넣기
    for i in range(n):
        # 피자를 넣기 (나중에 꺼낼때를 위해서 피자 번호도 같이!)
        next_i += 1
        orear += 1
        oven[orear] = [i, cheese[i]]    # 같이 넣는다.


    # 오븐에 남아있는 피자 개수?
    remain = n
    # 마지막에 꺼낸 피자의 번호
    last_index = -1

    # 모든 피자의 치즈가 녹을때까지 반복!
    while True:
        # 피자를 꺼내서
        ofront += 1
        i, pizza = oven[ofront]
        # 치즈를 녹이고 c // 2
        pizza //= 2
        # 치즈가 0이 아니라면 다시 오븐에 넣기
        if pizza != 0:
            orear += 1
            oven[orear] = [i, pizza]
        # 치즈가 0이다.
        else:
            # 현재 오븐의 자리에 남은 피자 하나를 꺼내서 넣기!
            if next_i < m:
                orear += 1
                oven[orear] = [next_i, cheese[next_i]]
                # 하나 꺼냈으니까 다음 피자 위치 바꾸기
                next_i += 1
            # 넣을 피자가 없다.
            else:
                # 오븐에 남은 피자도 없는 상황이 온다.
                remain -= 1
                if remain == 0:
                    # 현재 피자의 번호가 답이 된다.
                    last_index = i
                    # 반복 종료
                    break

    print(f'#{tc} {last_index + 1}')