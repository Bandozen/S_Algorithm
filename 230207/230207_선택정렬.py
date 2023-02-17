# 선택정렬
# 맨 앞자리부터 자리의 주인을 정해준다. (최솟값)
# i = 0 => 제일 작은 수
# i = 1 => 두번째로 작은 수
# i = 2 => 세번째로 작은 수...

def selection_sort(arr, n):
    # 맨 앞자리부터 자리의 주인을 정해준다. 작은숫자부터 차례대로
    for i in range(n - 1):
        min_idx = i
        # i 의 뒤부터 비교를 시작하면서 최솟값을 찾는다.
        for j in range(i+1, n):
            # 제일 작은 숫자의 인덱스를 찾기
            if arr[min_idx] > arr[j]:
                min_idx = j
        # 반복을 다 돌았으면 제일 작은 숫자를 찾은 거니까 현재 자리 i로 이동
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = [10, 25, 64, 22, 11]
n = len(arr)
selection_sort(arr, n)
print(arr)

# 내림차순 해주기!
def selection_sort_dec(arr, n):
    # 맨 앞자리부터 자리의 주인을 정해준다. 큰숫자부터 차례대로
    for i in range(n - 1):
        max_idx = i
        # i 의 뒤부터 비교를 시작하면서 최댓값을 찾는다.
        for j in range(i+1, n):
            # 제일 작은 숫자의 인덱스를 찾기
            if arr[max_idx] < arr[j]:
                max_idx = j
        # 반복을 다 돌았으면 제일 작은 숫자를 찾은 거니까 현재 자리 i로 이동
        arr[i], arr[max_idx] = arr[max_idx], arr[i]

arr = [10, 25, 64, 22, 11]
n = len(arr)
selection_sort_dec(arr, n)
print(arr)