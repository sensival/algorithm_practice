# 일직선 상의 마을에 여러 채의 집이 위치해 있다. 이중에서 특정 위치의 집에 특별히 
# 한 개의 안테나를 설치하기로 결정했다. 효율성을 위해 안테나로부터 모든 집까지의 거리의 총 합이 최소가 되도록 설치하려고 한다. 
# 이 때 안테나는 집이 위치한 곳에만 설치할 수 있고, 논리적으로 동일한 위치에 여러 개의 집이 존재하는 것이 가능하다.
# 집들의 위치 값이 주어질 때, 안테나를 설치할 위치를 선택하는 프로그램을 작성하시오.
# 예를 들어 N=4이고, 각 위치가 1, 5, 7, 9일 때를 가정하자.
# 이 경우 5의 위치에 설치했을 때, 안테나로부터 모든 집까지의 거리의 총 합이 (4+0+2+4)=10으로, 최소가 된다.

# 입력
# 4
# 5 1 7 9

# 출력
# 5

# 나의 풀이
n = int(input())
village = list(map(int, input().split()))

sum = []

for i in range(n):
    t_length = 0
    for house in village:
        t_length += abs(village[i]-house)
    
    sum.append((village[i], t_length))


sum.sort(key= lambda x: x[1])

print(sum[0][0])


# 교재 풀이
# 그냥 정렬 후 중간 값..

n = int(input())
data = list(map(int, input().split()))
data.sort()

# 중간값 출력
print(data[(n-1)//2])



