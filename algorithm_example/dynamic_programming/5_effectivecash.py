# N가지 종류의 화폐가 있다. N개의 화폐를 사용해서 합이 M이 되게하기 위한 최소한의 화폐 개수를 출력하고 불가능한 경우 -1 을 출력
# 입력예시
# 2 15
# 2
# 3 출력 5

# 3 4
# 3
# 5
# 7 출력 -1


n, m = map(int, input().split()) #2 15
array = []
for i in range(n): 
    array.append(int(input())) # array = [2, 3]

d = [10001] * (m + 1)
d[0] = 0

for i in range(n): # 0 1
    for j in range(array[i], m + 1): # 2~m 3~m까지
        if d[j-array[i]] != 10001:
            # i == 0 ) 2~m 
            # d[2-array[0]] == d[2-2] == d[0] == 0
            # d[3-array[0]] == d[1] == 10001 

            # i == 1 ) 3~m 
            # d[3-array[1]] == d[3-3] == d[0] == 0
            # d[4-array[1]] == d[1] == 10001

            d[j] = min(d[j], d[j-array[i]]+1)
            # i == 0 ) 2~m 
            # d[2] = min(d[2], d[2-2]+1) == min(10001, 0+1) == 1

            # i == 1 ) 3~m 
            # d[3] = min(10001, d[3-3]+1) == min(10001, 0+1) == 1

if d[m] == 10001:
    print(-1)
else:
    print(d[m])


