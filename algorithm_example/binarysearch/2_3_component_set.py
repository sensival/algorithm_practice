# 전자매장엔 부품이 n 개 있다. 각 부품은 고유한 정수형태의 번호가 있다. 어느날 손님이 m개 종류의 부품을 요청했다. 이때 손님이 요청한 부품이 있으면 yes, 없으면 no를 출력
# 입력 예시
# 5
# 8 3 7 9 2
# 3
# 5 7 9 출력 no yes yes

# Get the number of components in the store
n = int(input())
array = set(map, input().split())

# Get the number of components requested by the customer
m = int(input())
x = list(map(int, input().split()))

# Check the components requested by the customer one by one
for i in x:
    if i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

