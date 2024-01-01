# 힉셍들에게 0~n까지의 번호를 부여했다. 처음에는 모두 다른 팀에 속해 있어 n+1개의 팀이 존재한다. 
# 팀 합치기 연산은 두팀을 합치며 0 a b 의 형태로 주어진다.
# 같은 팅 확인 연산은 1 a b의 형태로 주어지며 YES or NO의 출력을한다
# 첫째줄에 n과 연산수 m이 주어진다.
# 입력예시
# 7 8 
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1  
# 출력 
# NO
# NO
# YES

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

# 노드와 연산 개수
n, m = map(int, input().split())

parent = [0] * (n + 1)

# 자기자신으로 초기화
for i in range(0, n + 1):
    parent[i] = i

for _ in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(parent, a,b)

    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")