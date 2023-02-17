prime = []
for i in range(2, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime.append(i)

t = int(input())
for tc in range(1, t+1):
    num = int(input())
    cnt = 0
    for i in range(len(prime)):
        if prime[i] > num:
            break
        for j in range(i, len(prime)):
            if prime[j] > num:
                break
            for k in range(j, len(prime)):
                if prime[k] > num:
                    break

                if prime[i] + prime[j] + prime[k] == num:
                    cnt+=1
    print(f'#{tc} {cnt}')