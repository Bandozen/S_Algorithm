t = int(input())
for tc in range(1, t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    arr1 = arr
    arr2 = [[arr[i][j] for i in range(9)] for j in range(9)]
    arr3 = [[arr[i % 3 * 3 + j //3][i // 3 * 3 + j % 3] for j in range(9)] for i in range(9)]
    answer = 1
    for r, c, s in zip(arr1, arr2, arr3):
        if len(set(r)) == len(set(c)) == len(set(s)) == 9:
            continue
        else:
            answer = 0
            break
    print(f'#{tc} {answer}')