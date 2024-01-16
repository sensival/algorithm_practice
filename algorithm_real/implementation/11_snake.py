# 뱀은 NxN의 보드 위를 기어다니다가 자신의 몸과 부딪히면 게임이끝나고 사과를 먹으면 몸이 늘어난다.
# 보드 상하좌우는 벽으로 되어있고 몇몇칸에는 사과가 놓여져 있다. 게임시작할때 뱀길이는 1이고 맨위 맨 왼쪽에 놓여진다. 뱀은 처음에 오른쪽을 향한다
# 뱀은 먼저 몸길이를 늘려 한칸이동후 사과가 있으면 사과를 먹은 후 꼬리는 움직이지않는다. 만약 사과가 없다면 한칸 몸을 늘린 후 한칸 꼬리를 늘려 이동한다.
# 뱀은 매초마다 이동을 하며 사과의 위치와 뱀의 경로가 주어질때 게임이 몇초에 끝나는지 출력한다
# 첫째줄에 보드의 크기가 주어진다. 다음줄에 사과의 개수가 주어진다. 다음줄부터 사과의 위치가 행 열로 주어진다.(1행 1열에는 사과가 없음)
# 다음 줄에는 방향 변환횟수 L이 주어짐. 다음 줄부터 게임시작으로 부터 X초가 지난 후 D방향(오른쪽 90도) 또는 L방향(왼쪽 90도) 

# 입력예시 1
# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D 출력 9

# 입력예시 2
# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L 출력 21

# 입력예시 3
# 10
# 5
# 1 5 
# 1 3
# 1 2
# 1 6
# 1 7
# 4 
# 8 D
# 10 D
# 11 D
# 13 L 출력 13

# 교재 풀이
n = int(input())
k = int(input())
data = [[0]*(n + 1) for i in range(n + 1)]
info = []

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c  = input().split()
    info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2
    direction = 0 # 처음에는 동쪽을
    time = 0 # 지난 초시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))

        # 벽이나 뱀의 몸통과 부딪혔을 때
        else:
            time += 1
            break

        x, y = nx, ny
        time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    
    return time

print(simulate())



