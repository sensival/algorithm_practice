# 세로 N x 가로M 얼음틀 크기와 얼음 틀 모양이 0과 1로 주어진다. 0은 구멍이 뚫려있는곳 이고 1은 칸막이. 몇개의 아이스크림이 만들어 질수 있는지 찾는 문제
# 입력예시 
# 4 5
# 00110
# 00011
# 11111
# 00000  출력 3

n, m= map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x,y):
    if  x<=-1 or x >=n or y<=-1 or y >=m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)