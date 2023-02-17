t = int(input())
for tc in range(1, t+1):
    a, b = input().split()
    i = 0
    cnt = 0
    while i < len(a):
        if a[i] == b[0]:
            if a[i:i+len(b)] == b:
                i+=len(b)
                cnt+=1
            else:
                i+=1
                cnt+=1
        else:
            i+=1
            cnt+=1
    print(f'#{tc} {cnt}')