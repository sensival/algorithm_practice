# N x N 크기의 시험관에는 1~K가지의 바이러스가 있다. 바이러스들은 모두 매초 상하 좌우로 증식하되, 숫자가 작은것부터 증식한다.
# S초가 지난 뒤 X, Y에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오
# 첫째줄에 n,k가 주어지며 둘째줄에는 S X Y가 주어진다.
# 입력예시 1
# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2 출력 3 

# 입력예시 2
# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 1 2 2 출력 0

from collections import deque

n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            # 바이러스 종류, 시간, X, Y 입력
            data.append((graph[i][j], 0, i, j))

# 낮은번호의 바이러스부터 큐에 넣기
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 증식하는 네가지 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 모든 큐의 원소하나씩 순회하는게 1초
while q:
    virus, s, x, y = q.popleft()

    if s == target_s:
        break
    

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny)) # 전염시켰으니 다시 맨 뒤로



print(graph[target_x-1][target_y-1])