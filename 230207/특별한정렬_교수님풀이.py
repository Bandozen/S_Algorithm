t = int(input())

for tc in range(1, t+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    # 기준 위치(탐색을 시작할 위치)
    i = 0
    # 바꿀 대상 위치(최대값 or 최소값)
    index = 0

    for ni in range(10):
        # 정렬 시작
        # 기준 위치에서 최대값 또는 최소값을 찾기 시작
        for j in range(ni, n):
            if ni % 2 == 0 and numbers[j] > numbers[index]:
                # 최대값의 인덱스
                index = j
            if ni % 2 == 1 and numbers[j] < numbers[index]:
                # 최소값의 인덱스
                index = j
        # 현재 위치와 최대값 또는 최소값의 위치에 있는 원소 자리를 바꾼다.
        numbers[ni], numbers[index] = numbers[index], numbers[ni]

    print(f'#{tc}', " ".join(map(str, numbers[:10])))