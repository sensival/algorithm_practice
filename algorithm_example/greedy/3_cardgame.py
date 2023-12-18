# 숫자가 쓰인 카드들이 MxN 형태로 놓여있다. 뽑고자 하는 카드가 있는 행을 선택한 후 그 행에서 가장 낮은 숫자 카드를 뽑아야한다. 최종적으로 뽑을수 있는 카드중 가장 높은 숫자의 카드를 고르는 문제
# 각 행마다 가장 작은 수를 찾고 그 수중 가장 큰 수를 뽑는 문제 
# 입력예시 
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2  출력 2

n,m=map(int, input().split())

result=0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result=max(result, min_value)

print(result)

'''
#이중 for 문 사용 풀이

n,m=map(int, input().split())

result=0
for i in range(n):
    data = list(map(int, input().split()))
    min_value=10001
    for a in data
        min_value = min(min_value, a)
    result= max(result, min_value)

    print(result)
'''