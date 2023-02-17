t = int(input())
for tc in range(1, t+1):
    n = int(input())    # 노선의 수

    nums = [0] * 1001
    num = 0
    for _ in range(n):
        t, s, e = map(int,input().split())
        if t == 1:
            for i in range(s, e+1):
                nums[i] += 1
        elif t == 2:
            for i in range(s, e+1, 2):
                nums[i] += 1
        elif t == 3:
            if s % 2 == 0:
                for i in range(s, e+1):
                    if i % 4 == 0:
                        nums[i] += 1
            elif s % 2 == 1:
                for i in range(s, e+1):
                    if i % 3 == 0 and i % 10 != 0:
                        nums[i] += 1

        for i in nums:
            if num < i:
                num = i
    print(f'#{tc} {num}')