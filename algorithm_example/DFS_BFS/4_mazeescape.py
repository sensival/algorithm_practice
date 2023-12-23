# # 세로 N x 가로 M 크기의 직사각형 크기의 미로에 1,1에서 n,m까지 이동하는 칸수를(첫째칸과 마지막칸 포함) 구하는 문제 괴물이 있는 부분은 0으로 없는 부분은 1로 표시된다.
# 입력예시
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111 출력 10

from collections import deque

n, m= map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    for i in range(4):
        nx =x + dx[i]
        ny =y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if graph[nx][ny] == 0:
            continue
        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[nx][ny] + 1
            queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))