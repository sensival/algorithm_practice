# 1~N번까지의 헛간 중 하나에 숨을 수 있으며 전체 맵에는 총 m개의 양방향 통로가 존재한다.
# 동빈이는 1번 헛간으로 부터 최단거리가 가장 먼 헛간을 가장 안전하다고 판단하고 있다. 최단거리는 지나야하는 통로의 개수를 말한다.
# 첫번째는 동빈이가 숨을 헛간 번호(여러개면 가장 작은 번호) 두번째는 헛간까지의 거리를, 세번째는 그 헛간과 같은 거리를 갖는 헛간의 개수를 출력하시오

# 입력예시
# 6 7
# 3 6
# 4 3
# 3 2
# 1 3
# 1 2
# 2 4
# 5 2

# 출력
# 4 2 3

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = 1
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    # a b 노드의 비용이 1
    graph[a].append((b, 1))
    graph[b].append((a, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now  = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

max_node = 0
max_distance = 0
result = []

for i in range(1, n + 1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]

    elif max_distance == distance[i]:
        result.append(i)


print(max_node, max_distance, len(result))