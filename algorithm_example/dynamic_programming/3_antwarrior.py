# 개미 전사들은 식량을 얻고자 한다 식량창고의 개수 n이 주어지고 각 칸마다 몇개의 식량이 들어있는지 주어진다. 식량창고는 최소 한칸이상 떨어져서 털어야 한다. 이때 개미들이 털수 있는 최대 식량의 양은?
# 입력예시
# 4
# 1 3 1 5 출력 8


# 교재 풀이
n =  int(input())

array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])


'''
6
5 1 1 5 1 5 해보기
'''