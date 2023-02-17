from pprint import pprint
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [[0] * n for i in range(n)]
    pprint(arr)
    for i in range(n):
        for j in range(i+1):
            if j == 0 or i == j:
                arr[i][j] = 1

            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

    pprint(arr)
    print(f'#{tc}')
    for x in arr:
        for item in x:
            if item:
                answer = [item]
                print(answer)

    for x in arr:
        answer = [v for v in x if v]
        print(*answer)
