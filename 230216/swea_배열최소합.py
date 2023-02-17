def backtracking(row, total):
    global answer

    if row == n:
        if total < answer:
            answer = total
            return

    if total > answer:
        return

    for i in range(n):
        if i not in visited:
            visited.append(i)
            backtracking(row + 1, total + arr[row][i])
            visited.pop()

t= int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = []
    answer = n * 10
    backtracking(0, 0)
    print(f'#{tc} {answer}')