stack = [0] * 3
top = -1

top += 1    # push(10)
stack[top] = 10

top += 1    # push(20)
stack[top] = 20

top += 1    # push(30)
stack[top] = 30

top -= 1
print(stack[top + 1])

top -= 1
print(stack[top + 1])

top -= 1
print(stack[top + 1])

# 약간의 안전장치
# 조건문을 걸어줌으로써 30이 다시 출력되지 않음!
if top > -1:
    top -= 1
    print(stack[top + 1])