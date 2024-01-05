# N개의 동전을 가지고 만들 수 없는 양의 정수 금액 중 최솟값을 구하세요
# 입력 예시 
# 5
# 3 2 1 1 9 출력 예시 8

# 나의 풀이 ----> 아직 못함
'''
n = int(input())

unit = list(map(int, input().split()))

sum = 0
sum_list = []
result = 1000000000

unit.sort()

if unit[0] != 1:
    result = 1

else:
    for won in unit:
        sum += won

    unit.sort(reverse=True)

    for i in range(n):
        sum = sum - unit[i] + 1
        if ????????????????????????????????
            result =  min(result, sum)
        else:
            continue


print(result)

'''

# 교재 풀이
n = int(input()) 
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)
