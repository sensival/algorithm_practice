# 마을에 n개의 집과 그 집을 연결하는 m개의 길로 이루어져 있다. 길마다 유지비가 있다. 마을의 이장은 2개의 분리된 마을로 만들 계획을 세우고 있다. 
# 분리된 두 마을 사이에는 길이 필요 없고 마을 안에서도 집마다 경로가 항상 존재하게 하면서 길을 최소화 하고 싶다.
# 첫째 줄에 집의개수 n 길의 개수 m이 주어진다.
# 그 다음 줄 부터 질의 정보가 주어진다 a b c -> a집과 b집을 연결하고 유지비는 c
# 입력 예시
# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4


# 나의 풀이
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

# 부모테이블 초기화
parent = [0] * (v + 1)

# 간선을 담을 리스트와 최종 비용을 담을 변수
edges =[]
result = 0

 # 자기자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i


for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()


for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent, b):
        now_cost = cost
        union_parent(parent, a, b)
        result += cost

print(result - now_cost)