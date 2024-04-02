# 왕국은 n개의 행성으로 이루어져 있다.
# 행성은 3차원 좌표위의 한 점으로 두 행성 A(x1,y1,z1) B(x2,y2,z2)을 잇는 터널의 비용은 min(|x1-x2|,|y1-y2|,|z1-z2|)이다
# 터널을 촐 n-1개 설치해서 모든행성이 이어지게 하려고 한다. 이때 필요한 최소비용을 구하시오

# 입력예시

# 5
# 11 -15 -15
# 14 -5 -15
# -1 -1 -5
# 10 -4 -1
# 19 -4 19 
# 출력예시
# 4

# 집합찾기
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


n = int(input())
parent = [0] * (n + 1)

edges = []
result = 0


for i in range(1, n + 1):
    parent[i] = i


x = []
y = []
z = []


for i in range(1, n + 1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()


# 인접한 노드틀로부터 간선정보를 추출하여 처리

for i in range(n-1):
    edges.append((x[i + 1][0]-x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0]-y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0]-z[i][0], z[i][1], z[i + 1][1]))


edges.sort()


for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost



print(result)
