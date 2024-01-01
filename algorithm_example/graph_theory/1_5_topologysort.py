# 위상 정렬? 방향이 있는 그래프에서 진입차수가 0인 그래프부터 edge를 따라서 정렬
# 입력 예시
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4  출력 1 2 5 3 6 4 7

from collections import deque

v, e = map(int, input().split())

indegree = [0] * (v + 1)

graph = [[] for i in range(v + 1)]

# 간선 입력 & 진입차수 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = [] # 큐에서 pop 되면 여기에 모이면서 정렬
    q = deque()

    # 진입차수가 0인 차수 찾아 큐에 넣기
    for i in range(1, v+1):
        if indegree[i] == 0: 
            q.append(i)
        
    while q:
        # 큐에서 꺼내서 result로 넣음
        now = q.popleft()
        result.append(now) 

        # now와 연결된 간선 삭제
        for i in graph[now]:
            indegree[i] -= 1
            # 간선 삭제 했을때 차수 0이면 큐에 넣기
            if indegree[i] == 0:
                q.append(i)
        
    for i in result:
        print(i, end = ' ')


topology_sort()


