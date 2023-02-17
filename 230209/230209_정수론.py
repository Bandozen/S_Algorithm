# 최대 공약수 GCD : Greatest Common Divisor

# 최소 공배수 LCM : Least Common Multiple

# a > b라고 가정
# 최대공약수 구하는 법
def gcd(a, b):
    for i in range(b, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

# 유클리드 호제법
def new_gcd(a, b):
    # a % b == 0
    # return b
    # else
    # gcd(b, a % b)
    # 코드로 바꾸면!
    if b == 0:
        return a
    else:
        return new_gcd(b, a % b)

# 최소공배수 구하는 법
def lcm(a, b):
    return a * b // new_gcd(a, b)

a = 20
b = 15
print(new_gcd(a, b))
print(lcm(a, b))