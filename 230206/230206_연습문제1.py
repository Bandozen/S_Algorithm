import random

from pprint import pprint

n = 5


arr = [[random.randrange(1, 11) for _ in range(n)] for _ in range(n)]

pprint(arr)

# 절댓값의 총합
abs_sum = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 행 우선순회
for i in range(n):
    for j in range(n):
        # 현재 위치(i, j)
        now = arr[i][j]
        print(f"arr[{i}][{j}] : {arr[i][j]}")

        # 4방향 탐색을 하면서 이웃한 원소의 차이의 절댓값의 합
        # 주의할 점 : 상하좌우로 움직일때 유효한 범위(인덱스)인제 꼭 확인
        temp_abs = 0 # 현재 위치에서 절댓값 차이의 합
        for d in range(4):
            nx = i + dx[d]
            ny = j + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                # 절댓값 계산
                temp_abs += abs(arr[i][j] - arr[nx][ny])
        abs_sum += temp_abs

print(f"정답 : {abs_sum}")