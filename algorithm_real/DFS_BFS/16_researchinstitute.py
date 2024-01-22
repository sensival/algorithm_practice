# N(행)xM(열) 크기의 연구소에 바이러스가 퍼져 벽을 세우려고한다. 바이러스는 상하좌우로 퍼질 수 있다. 새로 세울수 있는 벽의 갯수는 3개이며, 반드시 3개를 세워야한다.
# 벽을 세운뒤 바이러스가 퍼질 수 없는 안전영역의 최댓값을 구하시오

# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0 출력 27

# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2 출력 9

# 8 8
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 출력 3

# 교재 풀이
# 구현 + dfs 문제임. 모든 벽을 세우는 경우의 수를 dfs로 확인


n, m = map(int, input().split())
data = []
temp = [[0]*m for _ in range(n)]

for _ in range(n):
    data.append(list(map(int, input().split())))


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 바이러스를 사방으로 퍼지게 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

# 안전 영역 크기 계산
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    
    return score

def dfs(count):
    global result
    # 울타리 3개가 설치되면 안전영역 검사
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        # 바이러스 퍼졌을 때 상황 temp에 구현
        for i in range(n):
            for j in range(m):      
                if temp[i][j] == 2:
                    virus(i, j)
        '''
        a = 0
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 0:
                    a += 1    
        if a == 9:
            for i in range(n):
                for j in range(m):
                    print(temp[i][j], end = ' ')
                
                print()
        print()
        '''

        result = max(result, get_score())
        return

    
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                # 울타리 3개 될때까지 하나씩 세우기
                data[i][j] = 1
                count += 1
                # 안전 영역 확인
                dfs(count)
                # 설치한 벽 다시 빼기
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)