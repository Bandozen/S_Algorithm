t = int(input())

for tc in range(1, t + 1):
    k, n ,m = map(int, input().split())
    m_list = list(map(int, input().split()))

    walk = 0

    charge_station = [0] * (n + 1)
    # 정답
    count = 0
    for i in m_list:
        charge_station[i] += 1

    while walk + k < n:
        for i in range(k, 0, -1):
            if charge_station[walk + i] == 1 :
                walk += i
                count += 1
                break
        else:
            count = 0
            break

    print(f'#{tc} {count}')

