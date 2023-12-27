# 떡볶이 떡의 길이가 모두 다른 떡집이 있다. 절단기의 높이를 H로 설정하면 숫자의 제한없이 떡을 n 개를 한꺼번에 자를 수 있다.
# 손님이 n cm의 떡을 주문했을때 적어도 m만큼 떡을 얻기위해 설정해야 할 절단기 높이의 최댓값을 구하시오
# 입력 예시
# 4 6
# 19 15 10 17 출력 15

# 나의 풀이
import sys

def binary_search(array, target, start, end):
    h = (start + end) // 2
    sum = 0

    for i in dduk:
        if i - h >= 0:
            sum += i - h 

    if sum == target:
        return h

    elif sum > target: 
        # Return the current height if there are no more nodes to explore
        if start >  end: 
            return h
        else:            
            return binary_search(array, target, h+1, end)
        
    else:
        return binary_search(array, target, start, h-1)


n, m = map(int, input().split())
dduk = list(map(int, sys.stdin.readline().rstrip().split())) 
dduk.sort(reverse=True)

result = binary_search(dduk, m, 0, dduk[0])

print(result)

# 교재 풀이

n, m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    
    if total < m:
        end = mid - 1
    
    else:
        result = mid
        start = mid + 1


print(result)