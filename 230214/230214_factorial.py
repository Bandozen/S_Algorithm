# 팩토리얼을 재귀호출로 만들어보기!!
def fact(n):
    # 1. 종료 조건
    if n == 1:
        return 1
    # 2. 재귀 호출
    else:
        return n * fact(n - 1)

print(fact(5))