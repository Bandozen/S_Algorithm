code = {'0001101': 0, '0011001': 1, '0010011': 2,
        '0111101': 3, '0100011': 4, '0110001': 5,
        '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}


def solve():
    for val in arr:
        if '1' in val:
            # 오른쪽 끝의 '1'을 찾아야함
            e = len(val) - 1
            while val[e] == '0':
                e -= 1

            # 7개씩 암호 가져오기
            secret = []
            for i in range(e-55, e+1, 7):
                secret.append(code[val[i:i+7]])
            # 정상인 걸 확인해서 정상이면 값을 리턴 아니면 0을 리턴!
            if (sum(secret[0:8:2])*3 + sum(secret[1:8:2])) % 10 == 0:
                return sum(secret)
            else:
                return 0


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]

    print(f'#{tc} {solve()}')
