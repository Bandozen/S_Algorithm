t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = [i for i in range(1, 13)]
    a = len(arr)
    cnt = 0
    for i in range(1<<a):
        sub_set = []
        for j in range(a):
            if i & (1<<j):
                sub_set.append(arr[j])
        if len(sub_set) == n and sum(sub_set) == k:
            cnt += 1

    print(f'#{tc} {cnt}')