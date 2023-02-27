t = int(input())

for tc in range(1, t+1):
    n,m = map(int, input().split())
    cost = [list(map(int, input().split())) for _ in range(n)]
    maxV = 0 # 가장 비싼 나무
    maxC = 0 # 가장 비싼 나무를 심은 열번호, 1부터 시작함!
    total = 0
    cnt = 0
    # 열 우선 순회 (열번호 j가 나중에 나올때 가장 크다는 것이 보장 됨)
    for j in range(0, m, 2):
        for i in range(n):
            total += cost[i][j]
            cnt+=1
            if maxV <= cost[i][j]:
                maxV = cost[i][j]
                maxC = j

    print("열 우선 순회")
    print(f'#{tc} {total} {cnt} {maxV} {maxC + 1}')

    # 행 우선 순회 (나중에 나온 j가 가장 큰 열이라는 것을 보장할 수가 없음)
    maxV = 0  # 가장 비싼 나무
    maxC = 0  # 가장 비싼 나무를 심은 열번호, 1부터 시작함!
    total = 0
    cnt = 0
    for i in range(n):
        for j in range(0, m, 2):
            total += cost[i][j]
            cnt += 1
            if maxV <= cost[i][j]:
                maxV = cost[i][j]
                maxC = j

    print("행 우선 순회")
    print(f'#{tc} {total} {cnt} {maxV} {maxC + 1}')
