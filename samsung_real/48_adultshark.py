# 청소년 상어는 더욱 자라 어른 상어가 되었다. 상어가 사는 공간에 더 이상 물고기는 오지 않고 다른 상어들만이 남아있다. 
# 상어에는 1 이상 M 이하의 자연수 번호가 붙어 있고, 모든 번호는 서로 다르다. 상어들은 영역을 사수하기 위해 다른 상어들을 쫓아내려고 하는데, 
# 1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.

# N×N 크기의 격자 중 M개의 칸에 상어가 한 마리씩 들어 있다. 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다. 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고, 
# 자신의 냄새를 그 칸에 뿌린다. 냄새는 상어가 k번 이동하고 나면 사라진다.

# 각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다. 
# 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다. 우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다.
# 상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.

# 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면, 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.


# 우선 순위
# 상어 1	상어 2	상어 3	상어 4
# ↑	↓ ← ↑ →	↑	↓ → ← ↑	↑	→ ← ↓ ↑	↑	← → ↑ ↓
# ↓	→ ↑ ↓ ←	↓	↓ ↑ ← →	↓	↑ → ← ↓	↓	← ↓ → ↑
# ←	← → ↓ ↑	←	← → ↑ ↓	←	↑ ← ↓ →	←	↑ → ↓ ←
# →	→ ← ↑ ↓	→	→ ↑ ↓ ←	→	← ↓ ↑ →	→	↑ → ↓ ←

# 입력
# 첫 줄에는 N, M, k가 주어진다. (2 ≤ N ≤ 20, 2 ≤ M ≤ N2, 1 ≤ k ≤ 1,000)

# 그 다음 줄부터 N개의 줄에 걸쳐 격자의 모습이 주어진다. 0은 빈칸이고, 0이 아닌 수 x는 x번 상어가 들어있는 칸을 의미한다.

# 그 다음 줄에는 각 상어의 방향이 차례대로 주어진다. 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽을 의미한다.

# 그 다음 줄부터 각 상어의 방향 우선순위가 상어 당 4줄씩 차례대로 주어진다. 각 줄은 4개의 수로 이루어져 있다. 
# 하나의 상어를 나타내는 네 줄 중 첫 번째 줄은 해당 상어가 위를 향할 때의 방향 우선순위, 두 번째 줄은 아래를 향할 때의 우선순위,
# 세 번째 줄은 왼쪽을 향할 때의 우선순위, 네 번째 줄은 오른쪽을 향할 때의 우선순위이다. 각 우선순위에는 1부터 4까지의 자연수가 한 번씩 나타난다. 
# 가장 먼저 나오는 방향이 최우선이다. 예를 들어, 우선순위가 1 3 2 4라면, 방향의 순서는 위, 왼쪽, 아래, 오른쪽이다.

# 맨 처음에는 각 상어마다 인접한 빈 칸이 존재한다. 따라서 처음부터 이동을 못 하는 경우는 없다.

# 출력
# 1번 상어만 격자에 남게 되기까지 걸리는 시간을 출력한다. 단, 1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력한다.

# 예제 입력 1 
# 5 4 4
# 0 0 0 0 3
# 0 2 0 0 0
# 1 0 0 0 4
# 0 0 0 0 0
# 0 0 0 0 0
# 4 4 3 1
# 2 3 1 4
# 4 1 2 3
# 3 4 2 1
# 4 3 1 2
# 2 4 3 1
# 2 1 3 4
# 3 4 1 2
# 4 1 2 3
# 4 3 2 1
# 1 4 3 2
# 1 3 2 4
# 3 2 1 4
# 3 4 1 2
# 3 2 4 1
# 1 4 2 3
# 1 4 2 3
# 예제 출력 1 
# 14
# 문제에 나온 그림과 같다.

# 예제 입력 2 
# 4 2 6
# 1 0 0 0
# 0 0 0 0
# 0 0 0 0
# 0 0 0 2
# 4 3
# 1 2 3 4
# 2 3 4 1
# 3 4 1 2
# 4 1 2 3
# 1 2 3 4
# 2 3 4 1
# 3 4 1 2
# 4 1 2 3
# 예제 출력 2 
# 26
# 예제 입력 3 
# 5 4 1
# 0 0 0 0 3
# 0 2 0 0 0
# 1 0 0 0 4
# 0 0 0 0 0
# 0 0 0 0 0
# 4 4 3 1
# 2 3 1 4
# 4 1 2 3
# 3 4 2 1
# 4 3 1 2
# 2 4 3 1
# 2 1 3 4
# 3 4 1 2
# 4 1 2 3
# 4 3 2 1
# 1 4 3 2
# 1 3 2 4
# 3 2 1 4
# 3 4 1 2
# 3 2 4 1
# 1 4 2 3
# 1 4 2 3
# 예제 출력 3 
# -1
# 예제 입력 4 
# 5 4 10
# 0 0 0 0 3
# 0 0 0 0 0
# 1 2 0 0 0
# 0 0 0 0 4
# 0 0 0 0 0
# 4 4 3 1
# 2 3 1 4
# 4 1 2 3
# 3 4 2 1
# 4 3 1 2
# 2 4 3 1
# 2 1 3 4
# 3 4 1 2
# 4 1 2 3
# 4 3 2 1
# 1 4 3 2
# 1 3 2 4
# 3 2 1 4
# 3 4 1 2
# 3 2 4 1
# 1 4 2 3
# 1 4 2 3
# 예제 출력 4
# -1

n, m, k = map(int, input().split())

# 상어의 위치
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 상어의 방향
directions = list(map(int, input().split()))

# [냄새의 상어 번호, 냄새의 남은 시간]을 저장할 리스트
smell = [[[0, 0]] * n for _ in range(n)]

# 회전방향 우선순위 정보
properties = [[] for _ in range(m)]

# 각 상어의 회전 방향 우선순위정보
for i in range(m):
    for j in range(4):
        properties[i].append(list(map(int, input().split())))
                             
# 이동가능한 4가지 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 모든 냄새 정보 업데이트
def update_smell():
    for i in range(n):
        for j in range(n):
            # 냄새가 존재하면 시간 1 감소
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 상어가 존재하는 경우 냄새를 K로 설정
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]

# 모든 상어를 이동시키는 함수
def move():
    new_array = [[0] *  n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if array[x][y] != 0:
                direction = directions[array[x][y] - 1] # 현재 상어의 방향
                found = False
                # 일단 냄새가 존재하지 않는 곳이 있는지 확인
                for index in range(4):
                    nx = x + dx[properties[array[x][y] - 1][direction - 1][index]-1]
                    ny = y + dy[properties[array[x][y] - 1][direction - 1][index]-1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][1] == 0:
                            # 해당 상어의 방향 이동시키기
                            directions[array[x][y] - 1] = properties[array[x][y] - 1][direction - 1][index]
                            # 만약 이미 다른 상어가 있다면 번호가 낮은상어가 들어가도록
                            if new_array[nx][ny] == 0:
                                new_array[nx][ny] = array[x][y]
                            else:
                                new_array[nx][ny] = min(new_array[nx][ny], array[x][y])
                            found = True
                            break
                
                if found:
                    continue
                # 만약 주변에 냄새가 남아 있다면, 자신의 냄새가 있는 곳으로 이동
                for index in range(4):
                    nx = x + dx[properties[array[x][y] - 1][direction - 1][index]-1]
                    ny = y + dy[properties[array[x][y] - 1][direction - 1][index]-1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][0] == array[x][y]:
                            directions[array[x][y] - 1] = properties[array[x][y] - 1][direction - 1][index]
                            new_array[nx][ny] = array[x][y]
                            break
    return new_array

time = 0
while True:
    update_smell()
    new_array = move()
    array = new_array
    time +=1

    # 1번 상어만 남았는지 체크
    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False

    if check:
        print(time)
        break

    # 1000초 까지 끝나지 않았다면
    if time >= 1000:
        print(-1)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        break


