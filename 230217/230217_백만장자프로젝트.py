'''
1. 첫 번째 방법
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))[::-1]
    answer = maxV = 0
    for i in lst:
        if maxV > i:
            answer += maxV - i
        else:
            maxV = i
    print(f'#{tc} {answer}')
'''

'''
2. 두 번째 방법
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = list(map(int, input().split()))
    answer = i = 0
    while i < n:
        # [1] i ~ 끝까지 최대값의 index 찾기
        i_mx = i
        for j in range(i+1, n):
            if lst[i_mx] < lst[j]:
                i_mx = j
        # [2] i ~ i_mx 까지의 최대값과의 차이를 누적
        for j in range(i, i_mx):
            ans += lst[i_mx] - lst[j]

        i = i_mx + 1
    print(f'#{tc} {answer}')
'''