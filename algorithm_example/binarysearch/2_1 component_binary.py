# 전자매장엔 부품이 n 개 있다. 각 부품은 고유한 정수형태의 번호가 있다. 어느날 손님이 m개 종류의 부품을 요청했다. 이때 손님이 요청한 부품이 있으면 yes, 없으면 no를 출력
# 입력 예시
# 5
# 8 3 7 9 2
# 3
# 5 7 9 출력 no yes yes

# 나의 풀이
import sys

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) //2
    
    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    
    else:
        return binary_search(array, target, mid+1, end)
    
n = int(input())
component = list(map(int, sys.stdin.readline().rstrip().split())) 

m = int(input())
request = list(map(int, sys.stdin.readline().rstrip().split())) 

for i in range(m):
    if (binary_search(component, request[i], 0, n-1)):
        print("yes", end =' ')
    else:
        print("no", end = ' ')


# 교재 풀이
def binary_search(array, target, start, end):
    while(start <= end) :
        mid = (start + end) //2
        
        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            return binary_search(array, target, start, mid-1)
        
        else:
            return binary_search(array, target, mid+1, end)
        
    return None


n = int(input())
array = list(map, input().split())
array.sort()  # sort 먼저 해줘야한다!!!!

m = int(input())
x = list(map, input().split())

for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end =' ')
    else:
        print('no', end = ' ')
        