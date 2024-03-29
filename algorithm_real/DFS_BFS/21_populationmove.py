# N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다.
# 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.
# 오늘부터 인구 이동이 시작되는 날이다.
# 인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.
# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.
# 각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)

# 둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다. r행 c열에 주어지는 정수는 A[r][c]의 값이다. (0 ≤ A[r][c] ≤ 100)

# 인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어진다.

# 출력
# 인구 이동이 며칠 동안 발생하는지 첫째 줄에 출력한다.


# 예제 입력 1 
# 2 20 50
# 50 30
# 20 40

# 예제 출력 1 
# 1


# 예제 입력 2 
# 2 40 50
# 50 30
# 20 40

# 예제 출력 2 
# 0


# 예제 입력 3 
# 2 20 50
# 50 30
# 30 40

# 예제 출력 3 
# 1


# 예제 입력 4 
# 3 5 10
# 10 15 20
# 20 30 25
# 40 22 10

# 예제 출력 4 
# 2


# 예제 입력 5 
# 4 10 50
# 10 100 20 90
# 80 100 60 70
# 70 20 30 40
# 50 20 100 10

# 예제 출력 5 
# 3

from collections import deque

n, l, r = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0 # 왜 있는지 모르겠음

def process(x, y, index):
    united = []
    united.append((x, y))
    q = deque()
    q.append((x, y))
    # 연합 번호 매기기 -> 인구이동이 가능한 그룹끼리
    union[x][y] = index

    summary = graph[x][y]
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny]-graph[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))


    for i, j in united:
        graph[i][j] = summary // count
    

    return count

total_count = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    # 하루동안 생길수 있는 연합과 이동 탐색
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    
    # union[i][j] 가 모두 -1이면 아무런 연합도 생기지 않았다는 뜻 그래서 index가 n*n이 됨
    if index == n * n:
        break
    
    # 하루가 지났으므로 +1
    total_count += 1


print(total_count)
    

