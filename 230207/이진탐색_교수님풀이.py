t = int(input())

for tc in range(1, t + 1):
    p, a, b = map(int, input().split())
    '''
        p : 페이지 수
        a : a 가 찾아야 할때까지
        b : b 가 찾아야 할때까지
    '''
    winner = ""

    # a의 이진탐색 범위
    a_start, a_end = 1, p
    # b의 이진탐색 범위
    b_start, b_end = 1, p

    # 페이지를 찾을때 까지 반복 진행
    while True:
        a_find = False # a 가 페이지를 찾았는지
        b_find = False # b 가 페이지를 찾았는지

        # a 부터 페이지를 찾기 시작
        mid = (a_start + a_end) // 2

        if mid == a:
            a_find = True
        elif mid > a:
            a_end = mid
        else:
            a_start = mid

        # b도 페이지를 찾기
        mid = (b_start + b_end) // 2

        if mid == b:
            b_find = True
        elif mid > b:
            b_end = mid
        else:
            b_start = mid

        if a_find and b_find:
            winner = 0
            break
        if a_find:
            winner = "A"
            break
        if b_find:
            winner = "B"
            break

    print(f'#{tc} {winner}')