import random

heap = [0] * 101

last = 0

def enq(item):
    # 삽입을 했다면 마지막 위치를 수정해야함
    global last
    last += 1
    heap[last] = item

    # 추가를 하고나서 부모 노드 > 자식 노드를 만족하도록 해야한다.
    c = last    # 현재 위치를 자식으로 생각
    p = c // 2  # 부모노드의 위치 계산
    # 부모노드가 존재하고, 자식이 부모보다 작을 때까지 위치를 바꿔준다.
    while p and heap[p] < heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        # 자리를 바꿨으면
        # 자식의 위치를 다시 바꾸고 계속 진행
        c = p
        p = c // 2

def deq():
    global last
    # 루트 노드를 삭제하기 전에 기억
    tmp = heap[1]
    # 마지막 노드를 삭제해서 루트 위치에 땡겨온다.
    heap[1] = heap[last]
    last -= 1
    # 루트부터 자리 찾기 (비교해서 나보다 큰값이 자식중에 있으면 자리 교환)
    p = 1
    c = p * 2   # 왼쪽 자식을 기준으로 해서
    # 자식 위치로 가봤는데 자식이 last보다 작아야 트리 안에 존재한다.
    while c <= last:
        # 만약 오른쪽 자식이 있다면, 둘 중에 큰 자식과 비교를 한다.
        if c + 1 <= last and heap[c] < heap[c+1]:
            c = c + 1   # 비교대상을 오른쪽 자식으로
        if heap[p] < heap[c]:
            # 자식이 더 크면 자리를 교환
            heap[p], heap[c] = heap[c], heap[p]
            p = c
            c = p * 2
        else:
            # 그 밑에는 어차피 나보다 작은 애들만 있으니까 더이상 갈 필요가 없다!
            break

    return tmp


for i in range(10):
    enq(random.randrange(1,101))
print(heap)

for i in range(10):
    print(deq())
