t = int(input())

for tc in range(1, t+1):
    d, a, b, f = map(int, input().split())
    result = (d / (a+b)) * f
    print(f'#{tc} {result}')