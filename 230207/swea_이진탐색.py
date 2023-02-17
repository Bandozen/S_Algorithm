t = int(input())
def binary_search(page, t):
    start = 1
    end = page
    count = 1
    while start <= end:
        mid = (start + end) // 2
        if mid == t:
            return count
        elif mid < t:
            start = mid
            count += 1
        elif mid > t:
            end = mid
            count += 1

for tc in range(1, t+1):
    page, a, b = map(int, input().split())
    if binary_search(page,a) < binary_search(page, b):
        result = "A"
    elif binary_search(page,a) > binary_search(page, b):
        result = "B"
    else:
        result = 0
    print(f'#{tc} {result}')