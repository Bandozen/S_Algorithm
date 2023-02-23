'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

def preorder(i):
    if i:           # 존재하는 정점이면
        print(i, end = " ")
        preorder(left[i])
        preorder(right[i])
    return

def inorder(i):
    if i:
        inorder(left[i])
        print(i, end = " ")
        inorder(right[i])
    return

def postorder(i):
    if i:
        preorder(left[i])
        preorder(right[i])
        print(i, end = " ")
    return

v = int(input())
arr = list(map(int, input().split()))
e = v - 1                   # 간선 수
left = [0] * (v + 1)        # 부모를 인덱스로 왼쪽 자식 저장
right = [0] * (v + 1)       # 부모를 인덱스로 오른쪽 자식 저장
parent = [0] * (v + 1)
# child = [[] for _ in range(v+1)]
for i in range(e):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    # child[p].append(c)
    parent[c] = p

root = 1
while parent[root] != 0:
    root += 1
print(root)

preorder()
print()
inorder(root)
print()
postorder(root)
print()
