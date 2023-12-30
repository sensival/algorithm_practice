# N개의 도시가 있다. 각 도시는 연결된 통로를 통해 전보를 보낼 수 있다. X->Y 방향 통로가 있으면 전보를 보낼 수 있으나 반대 방향 통로가 없다면 메세지를 보낼 수 없다. 만약 다른 통로를 거쳐 전보를 보낸다면 비용이 소요된다.
# 어느날 C도시에서 위급한 상황이 발생했다. 각 도시 사이에 설치된 통로를 거쳐 메시지를 전달했을때 전달받는 도시의 수와 걸리는 시간을 출력하시오
# 첫째줄엔 도시의 개수 통로의 개수 C도시가 주어진다. 둘째줄부터 이어진 도시의 정보와 걸리는 시간이 주어진다.
# 입력예시
# 3 2 1
# 1 2 4
# 1 3 2

# 교재 풀이
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9) # 10억

n, m, start = map(int, input().split())

graph = [[] for i in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while(q):
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

# 도달할 수 있는 노드의 수
count = 0
# 도달할 수 있는 노드 중에서 가장 멀리있는 노드
max_distance = 0

for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작노드 제외라서 count - 1
print(count-1, max_distance)

