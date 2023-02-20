from collections import deque

def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data

def dequeue():
    global front
    front += 1
    return queue[front]


queue = [0] * 10
front = -1
rear = -1

rear += 1       # enqueue(1)
queue[rear] = 1
enqueue(2)
enqueue(3)

print(dequeue())
print(dequeue())
if front != rear:
    print(dequeue())
if front != rear:
    print(dequeue())

q = []
q.append(10)
q.append(20)
q.append(30)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

q1 = deque()
q1.append(100)
q1.append(200)
q1.append(300)
print(q1.popleft())
print(q1.popleft())
print(q1.popleft())