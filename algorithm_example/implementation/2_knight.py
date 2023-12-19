# 8x8 체스판 위의 나이트는 1) 수평으로 두칸 이동후 수직 한칸 2) 수직으로 두칸 이동 후 수평 한칸 만 이동 가능하다 (열:a~h행:1~8)이 주어졌을 때 움직일수 있는 경우의 수는?
# 입력예시 a1 출력 2

# 나의 풀이
location=input()
c_count=int(ord(location[0])-96)
r_count=int(location[1])
route_count=8

dx=[-2,-2,2,2,-1,-1,1,1]
dy=[-1,1,-1,1,-2,2,-2,2]

for i in range(8):
    nx=c_count+dx[i]
    ny=r_count+dy[i]

    if nx<1 or ny<1 or nx>8 or ny>8:
        route_count -= 1
    
print(route_count)

# 교재 풀이

input_data=input()
row= int(input_data[1])
column=int(ord(input_data[0]))-int(ord('a'))+1

steps=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

result=0

for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >=1 and next_row<=8 and next_column >=1 and next_column <=8:
        result += 1

print(result)