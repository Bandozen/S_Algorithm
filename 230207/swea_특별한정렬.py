t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num_list = list(map(int, input().split()))
    new_list = [0] * 10
    for i in range(n - 1):
        min_ = i
        for j in range(i + 1, n):
            if num_list[min_] > num_list[j]:
                min_ = j
        num_list[min_], num_list[i] = num_list[i], num_list[min_]
    for x in range(1, 10, 2):
        new_list[x] = num_list[x//2]
    print(new_list)
    for i in range(n-1):
        max_ = i
        for j in range(i + 1, n):
            if num_list[max_] < num_list[j]:
                max_ = j
        num_list[max_], num_list[i] = num_list[i], num_list[max_]
    for x in range(0, 10, 2):
        new_list[x] = num_list[x//2]

    print(f'#{tc}', *new_list)