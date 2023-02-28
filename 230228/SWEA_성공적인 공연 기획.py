t = int(input())
for tc in range(1, t+1):
    people = input()
    # 박수 총합
    clap = 0
    # 정답
    ans = 0
    for i in range(len(people)):
        if clap < i:
            clap += 1
            ans += 1
        clap += int(people[i])
    print(f'#{tc} {ans}')