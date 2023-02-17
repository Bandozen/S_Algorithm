T = int(input())

for tc in range(T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    c = [0] * (max(nums) + 1)

    for i in nums:
        c[i] += 1

    for i in range(1, len(c)):
        c[i] += c[i-1]

    result = [0] * len(nums)

    for i in range(len(result) - 1, -1, -1):
        c[nums[i]] -= 1
        result[c[nums[i]]] = nums[i]

    print(f'#{tc} {result}')