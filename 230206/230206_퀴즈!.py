# 퀴즈
# 행 : 5
# 열 : 6
# 값을 임의로 할당(random)
# 2차원 배열의 모든 원소를 순회하면서 짝수인 원소의 개수를 세는 프로그래밍
import random
from pprint import pprint
n = 5
m = 6
arr = [[random.randrange(1,11) for _ in range(m)]for _ in range(n)]

pprint(arr)
answer = 0
answer1 = 0
answer2 = 0

# 행 우선 순회
for i in range(n):
    for j in range(m):
        if arr[i][j] % 2 == 0:
            answer += 1

# 열 우선 순회
for j in range(m):
    for i in range(n):
        if arr[i][j] % 2 == 0:
            answer1 += 1

# 지그재그 순회
for i in range(n):
    for j in range(m):
        if arr[i][j + (m-1-2*j) * (i%2)] % 2 == 0:
            answer2 += 1
            
print("정답 :", answer, "개")
print("정답 :", answer1, "개")
print("정답 :", answer2, "개")