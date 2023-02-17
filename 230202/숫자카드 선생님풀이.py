t = int(input())

for tc in range(1, t+1):
    n = int(input()) # 숫자 카드의 개수
    numbers = input() # 숫자카드들이 주어지는데, 공백이 없이 붙어서 입력받는다.

    # 숫자 카드 개수를 세줄 카운트 배열
    counts = [0] * 10

    # numbers 에 있는 숫자 하나씩 보면서 개수 세기
    for num in numbers:
        counts[int(num)] += 1

    # 카드의 최대 개수
    max_count = 0
    # 가장 큰 카드 수(최대 개수가 같은게 여러개일 경우)
    max_num = 0

    for i in range(10):
        if counts[i] > max_count:
            max_count = counts[i]
            max_num = i
        if counts[i] == max_count:
            if max_num < i:
                max_num = i

    print(f'{tc} {max_num} {max_count}')

