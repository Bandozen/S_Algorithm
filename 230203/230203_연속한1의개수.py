t = int(input())

for tc in range(1, t+1):
    length = int(input())
    num_list = list(map(int, input()))
    ans = cnt = 0

    for i in range(length):
        if num_list[i] == 0:
            cnt = 0
        else:
            cnt += 1
            if ans<cnt:
                ans = cnt


    print(f'#{tc}', ans)