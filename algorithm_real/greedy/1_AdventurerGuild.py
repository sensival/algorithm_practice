# n명의 모험가가 있다. 공포도가 높은 모험가는 위험상황에 쉽게 대처하지 못한다. 공포도가 x인 모험가는 반드시 x명 이상으로 구성해야 한다. 이 때 여행을 떠날 수 있는 모험가 그룹의 최댓값은?(모든 모험가가 참여하지 않아도 된다.)
# 첫째 줄에 모험가 수 n이 주어지고, 둘째 줄에 각 모험가의 공포도 값이 n 이하의 자연수로 주어진다. 
# 입력 예시
# 5
# 2 3 1 2 2  출력: 2  (그룹1: 1,2,3 그룹2: 2 2)


# 나의 풀이
n = int(input())
fear = list(map(int, input().split()))

result = 0

fear.sort(reverse=True)

index = 0

while True:
    members = fear[index]
    n -= members
    result += 1
    if index > n-1 :
        break

print(result)
    