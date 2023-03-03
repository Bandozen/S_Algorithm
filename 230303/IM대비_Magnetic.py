t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [input().split() for _ in range(n)]
    ans = 0

    # [1] 첫번째 방법
    for st in zip(*arr):
        ans += "".join(st).replace('0','').count('12')

    # [2] 두번째 방법
    # arr_t = list(zip(*arr))
    # for i in arr_t:
    #     prev = 0
    #     for j in i:
    #         if i != '0':
    #             if i == '2' and prev == '1':
    #                 ans +=1
    #             prev = j

    print(f'#{tc} {ans}')