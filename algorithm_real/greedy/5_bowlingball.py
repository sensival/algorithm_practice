# 두 사람이 볼링을 치고 있다. 볼링공은 총 N개가 있으며 각 볼링공 마다 1~M까지의 무게가 있다. 두사람은 서로 다른 무게의 공을 고르려 한다. 이때 두사람이 고를 수 있는 볼링공의 조합을 구하시오(순서 상관x)
# 입력예시 1
# 5 3 
# 1 3 2 3 2 출력 예시 8
# 입력예시 2 
# 8 5
# 1 5 4 3 2 4 5 2 출력 예시 25


# 나의 풀이
n, m = map(int, input().split())

balls = list(map(int, input().split()))

result = n * (n-1)

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if balls[i] == balls[j]:
            result -= 1



print(int(result/2))




# 교재 풀이

n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11

# 볼링공 무게별 개수 세기
for x in data:
    array[x] += 1

result = 0

for i in range(1, m + 1):
    n -= array[i] # A가 선택하는 경우의 수 제외 --> N은 B가 선택하는 경우의 수가 됨. (index1, index2)와 (index2, index1) 는 같은 조합으로 보므로 누적해서 빼도 된다.
    result += array[i] * n # 둘이 곱해서 result에 더해주기

print(result)