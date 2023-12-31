# 입력 예시
# 3 3
# 1 2 
# 1 3 
# 2 3

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a 
    else:
        parent[a] = b

# 노드와 간선의 개수
v, e = map(int, input().split())

parent = [0] * (v + 1)

 # 자기자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False

# union 수행 중 사이클이 발생하면 break
for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) == find_parent(parent,b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)


if cycle:
    print("사이클이 발생하였습니다.")
else:
    print("사이클이 발생하지 않았습니다.")