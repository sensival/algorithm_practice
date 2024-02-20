# 고정점이란 그값이 인덱스와 동일한 원소를 말합니다. 하나의 수열이 서로다른 n개의 원소를 포함하고 있으며 수열에는 최대 한개의 고정점이 있었다.
# 시간복잡도 O(log n)으로 알고리즘을 설계

# 입력 예시
# 5
# -15 -6 1 3 7 출력 3

# 7
# -15 -4 2 8 9 13 15 출력 2

# 7
# -15 -4 3 8 9 13 15 출력 -1

def fix_point(array, start, end):
    if start > end :
        return None
    
    mid = (start + end) // 2

    if mid == array[mid]:
        return mid
    
    elif mid < array[mid]:
        return fix_point(array, start, mid - 1)
        
    else:
        return fix_point(array, mid + 1, end)

    
import sys

n = int(input())
input_string = sys.stdin.readline().rstrip()

# 입력된 문자열을 공백을 기준으로 분할하여 정수형으로 변환한 후 리스트에 저장
array = list(map(int, input_string.split()))

count = fix_point(array, 0, n - 1)

if count == None:
    print(-1)

else:
    print(count)

