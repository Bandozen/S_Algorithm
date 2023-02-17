def binary_search(arr, n, key):
    # 검색 범위 지정
    # 시작, 끝
    start = 0
    end = n-1


    while start <= end:
        # 가운데를 콕 찍는다
        mid = (start + end) // 2
        # 가운데에 내가 찾는 게 있다
        if arr[mid] == key:
            # 검색 성공!
            print("검색 성공!")
            return mid
        # 가운데 값이 내가 찾고있는 값보다 크다
        elif arr[mid] > key:
            # 검색 범위를 재지정
            # 오른쪽은 더이상 살펴볼 필요가 없다 => 뒤는 어차피 나보다 큰 애들만 있을거니까
            # 검색의 끝 범위를 가운데로 땡겨온다.
            end = mid - 1
        # 가운데 값이 내가 찾고 있는 값보다 작다
        else:
            # 검색 범위를 재지정
            # 왼쪽은 더이상 살펴볼 필요가 없다 => 앞은 어차피 나보다 작은 애들만 있을거니까!
            # 검색의 시작 범위를 가운데로 땡겨온다.
            start = mid + 1

    print("못 찾겠습니다...")
    return -1

# 반드시 정렬된 배열에서 사용해야 한다!
arr = [2, 3, 5, 7, 8, 16, 77]

n = len(arr)
print(binary_search(arr, n, 15))