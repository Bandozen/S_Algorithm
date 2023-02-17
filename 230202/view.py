T = 10

for tc in range(1, T + 1):

    n = int(input())

    buildings = list(map(int, input().split()))

    # 답
    count = 0

    # 앞부터 시작해서 끝까지 조망권 개수 구하기
    for i in range(2, n - 2):  # 빌딩 양쪽 2칸은 비어있음 (높이가 0)
        height = buildings[i]  # 현재 i 번째 위치 건물의 높이

        # 현재 건물의 꼭대기부터 시작해서 조망권이 확보된 칸수 구하기
        for floor in range(height, -1, -1):  # 위층부터 검사
            # 왼쪽, 오른쪽에 2칸씩 여유가 있는지 검사
            if floor > buildings[i - 1] and floor > buildings[i - 2] and floor > buildings[i + 1] and floor > buildings[
                i + 2]:
                count += 1
            else:
                # 조망권이 확보되지 않은 순간 밑층은 확인할 필요가 없으므로 반복 종료
                break

    print(f"#{tc} {count}")