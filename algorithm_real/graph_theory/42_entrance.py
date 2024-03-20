# 공항에는 1~G까지의 탑승구가 있다. P개의 비행기가 차례대로 도착할 예정이며 각 비행기는 1개의 탑승구에 도킹할수 있으며
# 비행기가 도킹할 수 있는 탑승구의 번호 i들이 주어진다(1~i번 안에 있는 탑승구 중 하나에 도킹가능)
# 어떠한 탑승구에도 도킹할 수 있는 비행기가 있을 경우 공항의 운행을 중지한다.
# 첫째 줄에는 탑승구의 개수, 둘째 줄에는 비행기의 수, 세번째 줄부터 비행기가 토킹할 수 있는 탑승구 범위가 주어 진다.
# 입력 예시
# 4
# 3
# 4
# 1
# 1

# 출력 
# 2

# 루트노드확인
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

g = int(input())
p = int(input())

parent = [0] * (g + 1)

for i in range(1, g + 1):
    parent[i] = i


result = 0
for _ in range(p):
    data = find_parent(parent, int(input()))
    if data == 0:
        break
    union_parent(parent, data, data - 1)
    result += 1

print(result)