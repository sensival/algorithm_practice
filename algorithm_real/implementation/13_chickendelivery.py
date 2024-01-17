# NxN의 도시가 있다. 도시의 각칸은 빈칸, 치킨집, 집 중 하나이다. '치킨 거리'는 집과 가장 가까운 치킨집 사이의 거리이며 |r1-r2|+|c1=c2|를 통해 구한다 
# '도시의 치킨거리'는 모든 집의 치킨거리의 합이다.
# 도시의 치킨집중 M개만 남기고 모두 폐업시키려고 한다. 폐업시키지않을 치킨집 M개를 골랐을때. 도시의 치킨거리의 최솟값을 구하시오.
# 첫째 줄에 도시의 크기 n과  폐업시키지않을 치킨집 M이 주어진다.
# 입력 예시 1
# 5 3 
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2 출력 5

# 입력 예시 2
# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2 출력 10

# 입력 예시 3
# 5 1
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0 출력 11

# 입력 예시 4
# 5 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1
# 1 2 0 2 1 출력 32


# 교재 풀이

from itertools import combinations
n, m = map(int, input().split())
chicken, house = [], []

# 한 행씩 입력 받으면서 집과 치킨집의 좌표를 append, 거리가 중요하니 index 0부터 시작하는 좌표여도 노상관
for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c)) 
        elif data[c] == 2:
            chicken.append((r,c))

# 모든 치킨집중 n개의 치킨집을 뽑는 조합
candidates = list(combinations(chicken, m))

# 후보들마다 치킨거리 합을 구함
def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx,cy in candidate: # 모든 치킨집에 대하여 거리 계산
            temp = min(temp, abs(hx- cx) + abs(hy - cy))
        
        result += temp

    return result


result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)