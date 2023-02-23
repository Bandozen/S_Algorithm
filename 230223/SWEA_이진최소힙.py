def enq(item):
    global last
    last += 1
    heap[last] = item
    c = last
    p = c // 2
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (n+1)
    last = 0
    for i in range(n):
        enq(arr[i])
    # print(heap)
    cnt = 0
    while n:
        n = n // 2
        cnt += heap[n]
    print(f'#{tc} {cnt}')