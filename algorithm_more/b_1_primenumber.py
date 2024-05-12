# M이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하시오
import math

m, n = map(int, input().split())
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(m, n + 1):
    if array[i]:
        print(i)
