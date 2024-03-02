# 성적표를 분실함
# 일부 성적을 비교한 자료만 있음
# A성적 < B성적 이면 A ->B로 화살표 그어놓음
# 학생들의 성적을 비교한 결과가 주어질 때 성적 순위를 정확히 알 수 있는 학생수?
# 첫째 줄에 학생 수 두 학생의 성적을 비교한 횟수
# 둘째줄부터 비교한 두 학생 나열 A B == A성적 < B성적

# 입력예시
# 6 6
# 1 5
# 3 4
# 4 2
# 4 6
# 5 2
# 5 4

# 출력예시
# 1

INF = int(1e9) #10억

# 노드 및 간선의 개수
n, m = map(int, input().split())
# 2차원 리스트를 만들고 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기자신 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선의 정보를 입력받아, 그 값으로 초기화
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

    
# 점화식에 따라 플로이드 워셜 알고리즘
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


result = 0

#각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 확인
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1

print(result)