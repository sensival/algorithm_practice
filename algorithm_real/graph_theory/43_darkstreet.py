# n개의 집과 m개의 도로로 구성되어있다. 각 집은 0 ~ n-1 까지의 번호로 구분되고 도로의 가로등을 하루동안 켜기위한 비용은 도로의 길이와 동일하다.
# 일부 가로등을 비활성화 하되 임의의 두 집에 대하여 가로등이 켜진 도로만으로도 오갈 수 있도록 만들고자 한다. 이때 일부 가로등을 비활성화 하여 절약할 수 있는 최대 금액을 출력하시오

# 입력예시
# 7 11
# 0 1 7 
# 0 3 5
# 1 2 8
# 1 3 9
# 1 4 7
# 2 4 5
# 3 4 15
# 3 5 6
# 4 5 8
# 4 6 9
# 5 6 11

# 출력
# 51
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)

edges = []
result = 0


for i in range(1, n + 1):
    parent[i] = i


for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((z, x, y))


edges.sort()
total = 0

for edge in edges:
    cost, a, b = edge
    total += cost

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(total - result)

