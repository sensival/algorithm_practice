# 전자매장엔 부품이 n 개 있다. 각 부품은 고유한 정수형태의 번호가 있다. 어느날 손님이 m개 종류의 부품을 요청했다. 이때 손님이 요청한 부품이 있으면 yes, 없으면 no를 출력
# 입력 예시
# 5
# 8 3 7 9 2
# 3
# 5 7 9 출력 no yes yes

n = int(input())
array= [0] * 1000001

for i in input().split():
    array[int(i)] += 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] >= 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

