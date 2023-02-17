def dfs(s, V):
    # 초기화
    visited = [0] * (V + 1)
    stack = []
    # 현재 방문한 정점을 i라고 합시다.
    i = s
    visited[i] = 1
    print(node[i])

    while True:
        # 현재 정점 i에서 탐색할 수 있는 다음 정점 w에 대해서
        # w로 가는 길이 있고, w를 방문한 적이 없다면 w 방문
        for w in adj_list[i]:
            if visited[w] == 0:
                stack.append(w)
                i = w
                visited[w] = 1
                print(node[i])
                break

        for w in range(1, V + 1):
            if adj[i][w] == 1 and visited[w] == 0:
                # w는 길이 있으니까 현재 위치 i를 스택에 저장
                stack.append(i)
                # 현재위치 i를 다음위치 w로 변경
                i = w
                print(node[i])
                # w는 방문했다 라고 표시
                visited[w] = 1
                # 현재위치 i에서 더 확인할 필요가 없음
                break
        # 내가 i에서 탐색을 했는데 더 이상 탐색할 정점이 없다.
        else:
            # 내가 최근에 방문했떤 정점을 스택에 넣어놨었지?
            # 그러면 하나 꺼내서 그 위치로 다시 돌아가야겠다!
            if stack:
                i = stack.pop()
            # 스택이 비어있는 경우 => 탐색 종료
            else:
                break

    # 함수 종료 전에 할 일
    return


# 인접 행렬
#       x A B C D E F G
adj = [[0,0,0,0,0,0,0,0], # x
       [0,0,1,1,0,0,0,0], # A
       [0,1,0,0,1,1,0,0], # B
       [0,1,0,0,0,1,0,0], # C
       [0,0,1,0,0,0,1,0], # D
       [0,0,1,1,0,0,1,0], # E
       [0,0,0,0,1,1,0,1], # F
       [0,0,0,0,0,0,1,0]] # G
node = ["", "A", "B", "C", "D", "E", "F", "G"]

'''
보통 인접행렬은 위에처럼 친절하게 나오지 않는다.
정점의 개수, 간선의 개수가 나온다.
ex) 7 8 => V, E
그리고 간선의 정보가 나온다.
start, to
1 2
1 3
2 4
2 5
3 7
4 6
5 6
6 7
'''
V, E = map(int, input().split())
adj = [[0] * (V + 1) for _ in range(V + 1)]
# 인접 리스트
adj_list = [[] for _ in range(V + 1)]
for i in range(E):
    start, to = map(int, input().split())
    adj[start][to] = 1
    # 무향 그래프(방향이 없는 그래프)만 아래 추가
    adj[to][start] = 1
    # 인접 리스트 사용
    adj_list[start].append(to)
    adj_list[to].append(start)


dfs(1, 7)