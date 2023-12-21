### 인접 행렬로 표현한 방식
INF= 999999999

graph=[[0,7,5],[7,0,INF],[5,INF,0]]

print(graph)





### 인접리스트로 표현한 방식

graph = [[]for _ in range(3)]

# 노드 0에 연결된 노드정보 (노드, 거리) 
graph[0].append((1,7)) 
graph[0].append((2,5))

# 노드 1에 연결된 노드정보 (노드, 거리) 
graph[1].append((0,7))

# 노드 2에 연결된 노드정보 (노드, 거리) 
graph[2].append((0,5))

print(graph)

