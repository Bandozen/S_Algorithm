def itoa(num):
    ret = ""

    # 숫자 하나씩 떼와서 (일의 자리부터) 문자열로 바꾸기
    while num > 0:
        i = num % 10
        ret += chr(ord('0') + i)
        num //= 10

    return ret[::-1]

s = itoa(123)
print(s)
print(type(s))