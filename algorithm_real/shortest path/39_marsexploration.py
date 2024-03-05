# 화성 탐사 기계가 N x N의 공간에 있고 각 공간을 이동하기위해서 필요한 에너지 소모량이 있다. 로봇은 상하좌우로 움직일 수 있으며
# [0][0]부터 [n-1][n-1]까지 이동하기 위한 최소비용을 출력하는 프로그램을 작성하시오
# 첫째줄에 테스트 케이스의 수가 주어진다. 각 테스트 케이스마다 n 과 각칸의 비용이 주어진다.
# 입력예시
# 3
# 3
# 5 5 4
# 3 9 1
# 3 2 7
# 5
# 3 7 2 0 1
# 2 8 0 9 1
# 1 2 1 8 1
# 9 8 9 2 0
# 3 6 5 1 5
# 7
# 9 0 5 1 1 5 3
# 4 1 2 1 6 5 3
# 0 7 6 1 6 8 5
# 1 1 7 8 3 2 3
# 9 4 0 7 6 4 1
# 5 8 3 2 4 8 3
# 7 4 8 4 8 3 4
# 교재풀이 다익스트라
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for tc in range(int(input())):
    n = int(input())

    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    distance = [[INF] * n for _ in range(n)]

    x, y  = 0, 0
    q = [(graph[x][y], x, y)]
    distance[x][y] = graph[x][y]

    while q:
        dist, x, y = heapq.heappop(q)
        # 이미 처리된 적 있는 노드면 skip
        if distance[x][y] < dist:
            print("여기?",n, x,y)
            continue
           
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(distance[n-1][n-1])