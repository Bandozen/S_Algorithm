# 회문검사 함수!
def check(lst):
    for i in range(len(lst)//2):
        if lst[i] != lst[-i-1]:
            return False
    return True

for tc in range(1, 11):
    t = int(input())
    lst = [list(input()) for _ in range(100)]
    t_lst = list(zip(*lst))
    maxV = 1

    for length in range(100, 1, -1):
        if maxV >= length:
            break
        for idx in range(100-length+1):
            if maxV == length:
                break
            for a, b in zip(lst, t_lst):
                if check(a[idx:idx+length]) or check(b[idx:idx+length]):
                    maxV = length
                    break
    print(f'#{tc} {maxV}')