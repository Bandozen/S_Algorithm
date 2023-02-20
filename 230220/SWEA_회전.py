t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    print(f'#{tc} {nums[m%n]}')