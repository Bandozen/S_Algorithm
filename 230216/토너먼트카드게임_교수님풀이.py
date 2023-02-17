가위 = 1
바위 = 2
보 = 3
def winner(a, b):
    if cards[a] == 가위:
        if cards[b] == 바위:
            return b
        elif cards[b] == 보:
            return a
        else:
            return a if a < b else b
    elif cards[a] == 바위:
        if cards[b] == 보:
            return b
        elif cards[b] == 가위:
            return a
        else:
            return a if a < b else b
    if cards[a] == 보:
        if cards[b] == 가위:
            return b
        elif cards[b] == 바위:
            return a
        else:
            return a if a < b else b
def tournament(i, j):
    # 1. 종료조건
    # 제일 작은 문제의 조건이 곧 종료 조건
    # 이때 해답을 구해서 return 해주면 된다.
    if i == j:
        return i

    # 2. 재귀호출
    # 작은 문제의 해답들을 이용해서 큰 문제의 해답을 구해 return
    left = tournament(i, (i+j) // 2)
    right = tournament((i+j) // 2 + 1, j)
    return winner(left, right)      # 큰 문제의 해답

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    cards = list(map(int, input().split()))
    win = tournament(0, n - 1)
    print(f'#{tc} {win + 1}')