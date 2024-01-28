# 로봇개발자 "무지"는 한 달 앞으로 다가온 "카카오배 로봇경진대회"에 출품할 로봇을 준비하고 있습니다. 
# 준비 중인 로봇은 2 x 1 크기의 로봇으로 "무지"는 "0"과 "1"로 이루어진 N x N 크기의 지도에서 2 x 1 크기인 로봇을 움직여 (N, N) 위치까지 이동 할 수 있도록 프로그래밍을 하려고 합니다. 
# 로봇이 이동하는 지도는 가장 왼쪽, 상단의 좌표를 (1, 1)로 하며 지도 내에 표시된 숫자 "0"은 빈칸을 "1"은 벽을 나타냅니다. 로봇은 벽이 있는 칸 또는 지도 밖으로는 이동할 수 없습니다. 
# 로봇은 처음에 아래 그림과 같이 좌표 (1, 1) 위치에서 가로방향으로 놓여있는 상태로 시작하며, 앞뒤 구분없이 움직일 수 있습니다.
# 로봇이 움직일 때는 현재 놓여있는 상태를 유지하면서 이동합니다. 예를 들어, 위 그림에서 오른쪽으로 한 칸 이동한다면 (1, 2), (1, 3) 두 칸을 차지하게 되며, 아래로 이동한다면 (2, 1), (2, 2) 두 칸을 차지하게 됩니다. 로봇이 차지하는 두 칸 중 어느 한 칸이라도 (N, N) 위치에 도착하면 됩니다.
# 로봇은 다음과 같이 조건에 따라 회전이 가능합니다.
# 위 그림과 같이 로봇은 90도씩 회전할 수 있습니다. 단, 로봇이 차지하는 두 칸 중, 어느 칸이든 축이 될 수 있지만, 회전하는 방향(축이 되는 칸으로부터 대각선 방향에 있는 칸)에는 벽이 없어야 합니다. 
# 로봇이 한 칸 이동하거나 90도 회전하는 데는 걸리는 시간은 정확히 1초 입니다.
# "0"과 "1"로 이루어진 지도인 board가 주어질 때, 로봇이 (N, N) 위치까지 이동하는데 필요한 최소 시간을 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# board의 한 변의 길이는 5 이상 100 이하입니다.
# board의 원소는 0 또는 1입니다.
# 로봇이 처음에 놓여 있는 칸 (1, 1), (1, 2)는 항상 0으로 주어집니다.
# 로봇이 항상 목적지에 도착할 수 있는 경우만 입력으로 주어집니다.

# 입출력 예
# board	                                                                            result
# [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]	7


from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 상하좌우 이동
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x+ dx[i], pos1_y + dy[i], pos2_x+ dx[i], pos2_y + dy[i] 
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)}) #?? 왜 집합
    # 가로 방향일 때 회전
    if pos1_x == pos2_x:
        for i in [-1, 1]:
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0:
                next_pos.append({(pos1_x, pos1_y),(pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y),(pos2_x + i, pos2_y)})
    # 세로 방향일 때 회전
    elif pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0:
                next_pos.append({(pos1_x, pos1_y),(pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y),(pos2_x, pos2_y + i)})

    return next_pos

def solution(board):
    n = len(board)
    # map을 1로 padding
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)
    # 너비 우선 탐색
    while q:
        pos, cost = q.popleft()
        # 제일 먼저 도착하는 경로 반환
        if (n, n) in pos:
            return cost

        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                # 이동가능한 경로 모두 q에 enqueue
                q.append((next_pos, cost + 1))
                #  왔던길 되돌아 가지 않게 visited
                visited.append(next_pos)

    
    return 0

import ast
def input_matrix_from_terminal():
    try:
        input_str = input()
        matrix = ast.literal_eval(input_str)
        
        # Validate the input to ensure it's a 2D list
        if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
            raise ValueError("Invalid input. Please enter a valid 2D list.")

        # Convert elements to integers
        result = [[int(element) for element in row] for row in matrix]
        return result
    except (ValueError, SyntaxError) as e:
        print(f"Error: {e}. Please enter a valid 2D list.")
        return None
    

board = input_matrix_from_terminal()
print(solution(board))