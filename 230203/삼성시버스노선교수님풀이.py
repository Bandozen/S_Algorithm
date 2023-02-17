t = int(input())

for tc in range(1, t+1):
    n = int(input()) # 버스 노선 개수

    bus_list = [list(map(int, input().split())) for _ in range(n)] # 각 노선 정보

    p = int(input()) # 정차 횟수 알고 싶은 정류장 갯수
    stop = [int(input()) for _ in range(p)] # 정차 횟수 알고 싶은 정류장 번호
    cnt_stop = [0] * p # 각 정류장의 정차 횟수 (0부터 시작)

    # 버스 노선 개수(n)만큼 반복 하면서
    for i in range(n):
    # stop의 갯수(p)만큼 반복
        for j in range(p):
            # stop의 각 원소(정차 횟수 알고싶은 정류장 번호)가 bus_list[i] 의 운행 정류장 범위에 포함되는지 검사
            # 만약 포함되면 cnt_stop[] += 1
            if bus_list[i][0] <= stop[j] <= bus_list[i][1]:
                cnt_stop[j] += 1

    print(f'#{tc}', *cnt_stop)