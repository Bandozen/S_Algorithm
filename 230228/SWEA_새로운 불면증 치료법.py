t = int(input())
for tc in range(1, t+1):
    n = int(input())
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    count = 0
    while nums:
        count += 1
        sheep = n * count
        sheep = str(sheep)

        for i in sheep:
            if i in nums:
                nums.remove(i)
    print(f'#{tc} {sheep}')