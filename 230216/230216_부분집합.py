def f(i, k, key):
    if i == k:          # 하나의 부분집합 완성
        s = 0
        for j in range(k):
            if bit[j]:
                s+= A[j]    # 부분집합의 합
        if s == key:
            return 1
        else:
            return 0
        # if s == key:        # 합이 key와 같은 부분집합을 출력
        #     for j in range(k):
        #         if bit[j]:
        #             print(A[j], end = ' ')
        #     print()
    else:
        bit[i] = 1
        if f(i+1, k, key):
            return 1
        bit[i] = 0
        if f(i+1, k, key):
            return 1
        return 0

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(A)
key = 10
bit = [0] * N
print(f(0, N, key))