# 현재위치, 현재 방향이 주어지면 반시계방향으로 회전하며 이동할 곳을 탐색한다. 왼쪽에 가보지 못한곳이 있으면 그곳으로 이동, 그렇지않으면 반시계방향으로 회전하며 이동할 곳을 탐색한다.
# 만약 네방향이 모두 가본칸이거나 바다인 경우 바라보는 방향을 유지한채 한 칸 뒤로 간다. 뒤쪽 방향이 바다여서 움직이지 못하는 경우 움직임을 멈춘다. 캐릭터가 방문한 칸 수를 출력한다.
# 입력예시
# 4 4 맵 크기 세로, 가로
# 1 1 0 위치와 방향(0북, 1동, 2남, 3서)
# 1 1 1 1 맵 입력 1 바다 0 육지
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1


# 교재 풀이
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위해 맵을 0으로 초기화(왜 굳이 이러는지 모르겠음. 어차피 나중에 map 입력받는데..?)
d = [[0]*m for _ in range(n)]
x, y ,dr = map(int, input().split())
d[x][y]=1 #현재 좌표 방문처리

array=[]
for i in range(n):
    array.append(list(map(int, input().split())))

#북 동 남 서 방향정의
dx=[-1,0,1,0]
dy=[0,1,0,-1]

def turn_left():
    global dr #함수 바깥에서 선언된 변수를 쓰려면 global을 써줘야 함
    dr-= 1
    if dr == -1:
        dr = 3

count = 1
turn_time = 0
while True:
    turn_left()
    nx=x+dx[dr]
    ny=y+dy[dr]
    if d[nx][ny]==0 and array[nx][xy]==0:
        d[nx][ny]=1
        x=nx
        y=ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1
    if turn_time ==4:
        nx=x-dx[dr]
        ny=y-dy[dr]
        if array[nx][ny]==0:
            x=nx
            y=ny
        else: 
            break
        turn_time=0

print(count)

