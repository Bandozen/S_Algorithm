import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    # 가로 칸의 수
    n = int(input())

    # 상자 탑 높이 정보
    box = list(map(int, input().split()))

    ans = 0

    # 반복문을 돌면서 현재 위치의 높이에서 제일 위에 있는 상자의 낙차 중에 가장 큰 값을 구하면 된다.
    for i in range(n):
        # 현재 위치에서 맨 꼭대기 상자가 오른쪽에 장애물이(상자) 없다고 했을 때 최대 낙차 구하기!
        height = n - (1 + i)
        # 또 반복문을 돌면서 현재 내 위치 기준 오른쪽에 있는 장애물(상자)의 수 구하기!
        cnt = 0
        for j in range(i+1, n):
            # 내 위치 기준 오른쪽에 있는 상자 수는 높이가 나와 같거나 큰 상자의 수를 구하면 된다.
            # 현재 위치 상자 높이는 box[i]
            # 현재 위치 기준 오른쪽 상자 높이는 box[j]
        # 최대 낙차 = 현재 위치에서 오른쪽에 상자가 없을 경우 최대 낙차 - 오른쪽 상자 수
            if box[i] <= box[j]:
                cnt += 1
        # 최대 낙차 중 최댓값을 갱신
        if ans < height - cnt:
            ans = height - cnt
    print(f"#{tc} {ans}")