# 입력예시
# 6 4
# 1 4
# 2 3
# 2 4
# 5 6
# 각 원소가 속한 집합: 1 1 1 1 5 5 
# 부모 테이블(부모노드): 1 1 2 1 5 5

# 특정 원소가 속한 집합 찾기
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a # a 쪽 루트가 더 작으면 b 의 루트도 a의 루트
    else:
        parent[a] = b

# 노드와 간선의 개수
v, e = map(int, input().split())

parent = [0] * (v + 1)

 # 자기자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 수행 [0,1,2,3,4,5,6]---> [0,1,1,2,1,5,5]
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print('각 원소가 속한 집합:', end=' ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')
    
print()

print('부모 테이블(부모노드):', end=' ')

for i in range(1, v + 1):
    print(parent[i], end =' ')
