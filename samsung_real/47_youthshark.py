# 아기 상어가 성장해 청소년 상어가 되었다.

# 4×4크기의 공간이 있고, 크기가 1×1인 정사각형 칸으로 나누어져 있다. 공간의 각 칸은 (x, y)와 같이 표현하며, x는 행의 번호, y는 열의 번호이다. 
# 한 칸에는 물고기가 한 마리 존재한다. 각 물고기는 번호와 방향을 가지고 있다. 번호는 1보다 크거나 같고, 16보다 작거나 같은 자연수이며, 두 물고기가 같은 번호를 갖는 경우는 없다. 
# 방향은 8가지 방향(상하좌우, 대각선) 중 하나이다.

# 오늘은 청소년 상어가 이 공간에 들어가 물고기를 먹으려고 한다. 청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다. 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다. 
# 이후 물고기가 이동한다.

# 물고기는 번호가 작은 물고기부터 순서대로 이동한다. 물고기는 한 칸을 이동할 수 있고, 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸, 이동할 수 없는 칸은 상어가 있거나, 
# 공간의 경계를 넘는 칸이다. 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다. 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 
# 그 외의 경우에는 그 칸으로 이동을 한다. 물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.

# 물고기의 이동이 모두 끝나면 상어가 이동한다. 상어는 방향에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다. 
# 상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다. 이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다. 
# 물고기가 없는 칸으로는 이동할 수 없다. 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다. 상어가 이동한 후에는 다시 물고기가 이동하며, 이후 이 과정이 계속해서 반복된다.


# 입력
# 첫째 줄부터 4개의 줄에 각 칸의 들어있는 물고기의 정보가 1번 행부터 순서대로 주어진다. 물고기의 정보는 두 정수 ai, bi로 이루어져 있고, ai는 물고기의 번호, bi는 방향을 의미한다. 방향 bi는 8보다 작거나 같은 자연수를 의미하고, 1부터 순서대로 ↑, ↖, ←, ↙, ↓, ↘, →, ↗ 를 의미한다.

# 출력
# 상어가 먹을 수 있는 물고기 번호의 합의 최댓값을 출력한다.

# 예제 입력 1 
# 7 6 2 3 15 6 9 8
# 3 1 1 8 14 7 10 1
# 6 1 13 6 4 3 11 4
# 16 1 8 7 5 2 12 2
# 예제 출력 1 
# 33
# 예제 입력 2 
# 16 7 1 4 4 3 12 8
# 14 7 7 6 3 4 10 2
# 5 2 15 2 8 3 6 4
# 11 8 2 4 13 5 9 4
# 예제 출력 2 
# 43
# 예제 입력 3 
# 12 6 14 5 4 5 6 7
# 15 1 11 7 3 7 7 5
# 10 3 8 3 16 6 1 1
# 5 8 2 7 13 6 9 2
# 예제 출력 3 
# 76
# 예제 입력 4 
# 2 6 10 8 6 7 9 4
# 1 7 16 6 4 2 5 8
# 3 7 8 6 7 6 14 8
# 12 7 15 4 11 3 13 3
# 예제 출력 4 
# 39

import copy

array = [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        array[i][j] = [data[j * 2], data[j * 2 + 1] - 1]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def turn_left(direction):
    return(direction + 1) % 8

result = 0

def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None


def move_all_fishes(array, now_x, now_y):
    for i in range(1, 17):
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                direction = turn_left(direction)


def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        if 0 <= now_x and now_x < 4 and 0 <= now_y and now_y <4:
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions


def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array)

    total += array[now_x][now_y][0]
    array[now_x][now_y][0] = -1

    move_all_fishes(array, now_x, now_y)

    positions = get_possible_positions(array, now_x, now_y)

    if len(positions) == 0:
        result = max(result, total)
        return
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)


dfs(array, 0, 0, 0)
print(result)