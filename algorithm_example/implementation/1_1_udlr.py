# N x N 정사각형 공간 (1,1)에 서있다. 이동할 계획서가 L R U D로 주어지면 최종 도착 좌표를 출력. 정사각형을 벗어나는 움직임은 무시한다
# 입력예시
# 5
# R R R U D D 출력 3 4

# 나의 풀이
'''
n=int(input())
plan = input().split()

r_count=1
c_count=1

for step in plan:
    if step == 'L':
        if r_count == 1:
            continue
        else:
            r_count -= 1

    elif step == 'R':
        if r_count == n:
            continue
        else:
            r_count += 1

    elif step == 'U':
        if c_count == 1 :
            continue
        else:
            c_count -= 1

    else :
        if c_count == n :
            continue
        else:
            c_count += 1


print(c_count,r_count)

'''
# 교재 풀이
n=int(input())
x,y=1,1
plans = input().split()
dx=[0,0,-1,1]
dy=[-1,1,0,0]
move_types=['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx=x+dx[i]
            ny=y+dy[i]

    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    x,y=nx,ny

print(x,y)
