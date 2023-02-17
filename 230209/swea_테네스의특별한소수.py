def is_prime():
    for i in range(n+1):
        if prime[i] == 1:
            for j in range(i*2, n+1, i):
                prime[j] = 0
n = 10**6
prime = [1]*(n+1)
prime[0], prime[1] = 0, 0
is_prime()


t = int(input())
for tc in range(1, t+1):
    d, a, b = map(int, input().split())
    cnt = []
    d = str(d)
    for i in range(a, b+1):
        if d in str(i) and prime[i]:
            cnt.append(i)

    print(f'#{tc}', len(cnt))