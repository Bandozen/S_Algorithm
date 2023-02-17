# 당근문제의 가로세로 버전!
def count(arr):
    maxV = 2
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1:
                cnt+=1
                if maxV < cnt:
                    maxV = cnt
            else:
                cnt = 0
    return maxV

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr_t = list(map(list, zip(*arr)))

    ans = count(arr)
    t = count(arr_t)
    if ans < t:
        ans = t
    print(f'#{tc} {ans}')