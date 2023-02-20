for _ in range(1, 11):
    t = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    # 인덱스번호
    idx = -1
    # 마지막 글자가 0이면 종료이므로 0이 될때까지 돌린다.
    while arr[idx] > 0:
        # 하나씩 올려서 첫번째 값부터 시작!
        idx += 1
        # 8개의 숫자가 있으니까 8로 나눈 나머지들을 계속 해준다.
        idx %= 8
        # 첫번쨰 숫자는 1 감소하고 계속해서 5까지 감소한 거를 현재값에서 뺴준다.
        arr[idx] -= cnt % 5 + 1
        # 다음 숫자로 넘어가기 위한 변수
        cnt += 1
        # 만약에 0이거나 음수가 된 수가 있다면
        if arr[idx] <= 0:
            # 0으로 바꿔준 다음
            arr[idx] = 0
    # 마지막으로 위치를 옮겨준다.
    answer = arr[idx+1:] + arr[:idx+1]
    print(f'#{t}', *answer)
