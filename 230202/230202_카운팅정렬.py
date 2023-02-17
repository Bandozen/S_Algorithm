arr = [3, 5, 4, 3, 4, 1, 2, 7, 8, 9, 0] # 입력된 배열
print(arr)
c = [0] * (max(arr) + 1) # 입력된 배열안의 데이터들을 카운트 할 수 있는 배열

for i in arr:
    c[i] += 1

print(c)

for i in range(1, len(c)):
    c[i] += c[i-1]

print(c)

result = [0] * len(arr) # 정렬된 배열

for i in range(len(result)-1, -1, -1):
    c[arr[i]] -= 1
    result[c[arr[i]]] = arr[i]

print(result)