def function1(num):
    print("now", num)
    # 1. 반드시 종료 조건을 정한다.
    if num == 0:
        return
    # 2. 종료조건이 아닌 경우에 재귀 호출
    # 언젠가는 종료조건을 만족하도록 변경 해줘야한다.
    else:
        function1(num - 1)

    print("back", num)

function1(5)