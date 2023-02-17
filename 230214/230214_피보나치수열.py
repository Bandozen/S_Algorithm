n = 20
memo = [0] * 20
memo[1] = 1

def fibo(n):
    # n번째 항을 계산한 적이 없고, n이 2 이상이라면
    # n번째 항을 계산 해야한다.
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo(n-1) + fibo(n-2)

    # 계산한 적이 있으면 memo[n] 값을 그대로 사용하면 된다.
    return memo[n]

print(fibo(7))
