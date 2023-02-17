'''
3
5
55 7 78 12 42
6
55 7 78 100 42 1
7
55 7 78 12 42 2 90
가장 큰 값을 출력하시오
#1 78
#2 100
#3 90
'''
T = int(input())
for tc in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = arr[0]           # 첫 원소를 최대로 가정!
    for i in range(N):   # 나머지 원소와 비교!
        if maxV < arr[i]:
            maxV = arr[i]
    print(f'#{tc+1} {maxV}')