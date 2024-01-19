# 도시에는 1~N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이고 모든 도시의 최단 거리가 K인 모든 도시의 번호를 출력하는 프로그램을 쓰시오. 아무 도시도 존재하지 않으면 -1 출력
# 첫째 줄에 도시개수 n, 도로개수 m, 거리정보 k, 출발도시번호 x가 주어진다. 둘째줄부터 두 개의 자연수가 주어지며 이는 두 도시 사이의 단방향 도로가 존재한다는 뜻이다.
# 입력 예시 1
# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4   출력 4

# 입력 예시 2
# 4 3 2 1
# 1 2
# 1 3
# 1 4 출력 -1

# 입력 예시 3
# 4 4 1 1
# 1 2
# 1 3
# 2 3
# 2 4 
# 출력 
# 2
# 3

# 교재 풀이

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 도로정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# x부터 모든 도시와의 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0

# 너비우선 탐색
q = deque([x])# 큐에 출발지점 enqueue
while q:
    now = q.popleft()
    for next_node in graph[now]: # 이어진 노드들 하나씩 확인
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1 # 현재 노드와 이어져있다면 1씩 더하기
            q.append(next_node)



check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True


if check == False:
    print(-1)