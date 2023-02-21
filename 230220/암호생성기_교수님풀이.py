for tc in range(1, 11):
    t = int(input())

    # 문자열 입력
    password = list(map(int, input().split()))

    n = 8

    # 원형 큐
    q = [0] * (n + 1)
    front = rear = 0

    # 처음 n 번 큐에 넣기
    for i in range(n):
        rear = (rear + 1) % n
        q[rear] = password[i]

    # 뺴줄 숫자 (5보다 커지면 1로 다시 돌아간다.)
    number = 1

    while True:
        # 비밀번호 하나 꺼내서
        # number를 빼준 후 다시 큐에 추가를 해주면 된다!
        front = (front + 1) % n
        item = q[front]
        item -= number

        # 숫자는 빼 봤는데 이 수가 만약 0이하가 되버렸다.
        # 비밀번호가 완성되는 순간!!
        # 0으로 바꾸고 큐이 맨 뒤에 삽입
        if item <= 0:
            item = 0
            rear = (rear + 1) % n
            q[rear] = item
            break
        else:
            # 0보다 크면 그냥 큐의 맨 뒤에 넣기
            rear = (rear + 1) % n
            q[rear] = item
            # 다음 뺄 수를 1씩 증가
            number += 1
            if number > 5:
                number = 1

    print(f'#{tc}', end = " ")
    # 원형큐를 사용했다면 그냥 출력할때도 앞에서 차례대로 빼면 된다.
    for i in range(8):
        front = (front + 1) % n
        print(q[front], end = " ")
    print()