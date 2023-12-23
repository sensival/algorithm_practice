# 첫째 줄에 입력할 수의 갯수가 주어진다. 둘째 줄에 1~ 100000 사이의 자연수가 입력된다. 수열을 내림차순으로 출력
# 입력 예시
# 3
# 15
# 27
# 12 출력 27 15 12

n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end = ' ')

    

