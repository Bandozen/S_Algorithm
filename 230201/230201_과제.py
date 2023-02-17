import sys

sys.stdin = open("input.txt")

for tc in range(1, 11):
    # 건물의 개수
    n = int(input())
    # n개의 건물의 높이
    height = list(map(int, input().split()))

    # 조망권이 확보된 세대의 수
    answer = 0
    # 왼쪽 2칸, 오른쪽 2칸은 0이므로 사이에서만 반복을 돌려야 함!
    for i in range(2, n-2):
        # i번째 해당하는 건물의 높이와 왼쪽으로 1,2칸 그리고 오른쪽으로 1,2칸 건물의 높이의 차를 각 변수에 담아줌
        first = height[i] - height[i-2]
        second = height[i] - height[i-1]
        third = height[i] - height[i+1]
        fourth = height[i] - height[i+2]
        # 그래서 이 높이의 차가 0보다 높으면

