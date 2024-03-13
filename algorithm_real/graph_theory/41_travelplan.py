# N개의 여행지가 있으며 각 여행지는 1~N번까지의 번호로 구분됩니다.
# 여행지가 도로로 연결되면 양방향 이동가능하다는 뜻입니다.
# 첫째줄 여행지 수 n 과 여행 계획 수 m 이 주어지고, 둘째 줄부터 nxn행렬로 여행지간 도로정보가 주어지고, 셋째줄에는 여행계획에 포함된 도시번호들이 주어진다.
# 여행계획이 가능하면 YES 불가능하면 NO를 출력하시오
# 입력예시
# 5 4 
# 0 1 0 1 1
# 1 0 1 1 0
# 0 1 0 0 0 
# 1 1 0 0 0
# 1 0 0 0 0
# 2 3 4 3

# 출력 
# YES

# 서로소 집합 알고리즘
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


n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모테이블 초기화

# 부모테이블 자기자신으로 
for i in range(1, n + 1):
    parent[i] = i

# union
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i + 1, j + 1)

# 여행 계획 입력받기
plan = list(map(int, input().split()))

result = True

# 모든 노드의 루트노드가 동일한지 확인
for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        result = False

if result:
    print("Yes")
else:
    print("No")