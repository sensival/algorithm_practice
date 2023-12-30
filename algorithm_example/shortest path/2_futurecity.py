# 미래 도시에는 1~ N번까지의 회사가 있는데 특정 회사끼리는 서로 도로로 연결되어있다(1만큼의 시간으로 연결). K번 회사에서 소개팅을 하고 X번회사에 방문해 물건을 판매하려고 할때 최소시간을 구하시오. 갈수 없다면 -1
# 첫째줄에 회사의 개수와 경로의 개수가 차례대로 주어진다. 둘째줄부터 연결된 회사가 주어진다. 마지막 줄에는 방문해야하는 x번 회사와 k번 회사가 주어진다 (K->X 순서로 방문)
# 입력 예시
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# 교재풀이

INF = int(1e9)

n , m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
x, k = map(int, input().split())

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("1")
else:
    print(distance)