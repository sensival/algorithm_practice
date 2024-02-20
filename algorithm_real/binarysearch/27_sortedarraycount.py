# n개의 원소를 포함하는 수열이 오름차순으로 정렬되어있다. 이때 수열에서 x가 등장하는 횟수를 구하시오. 없으면 -1 이며 O(logN)으로 시간복잡도 설계

# 입력예시
# 7 2
# 1 1 2 2 2 2 3  출력 4

# 7 4 
# 1 1 2 2 2 2 3 출력 -1

# 교재풀이 1
'''
def count_by_value(array, x):
    # 데이터의 갸ㅐ수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a =   first(array, x , 0, n - 1)

    if a == None:
        return 0
    
    b = last(array, x, 0, n - 1)

    return b - a + 1


def first(array, target, start, end):
    if start > end :
        return None
    mid = (start + end) // 2

    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    
    elif array[mid] >= target:
        return first(array, target, start, mid -1)
    
    else:
        return first(array, target, mid + 1, end)
    

def last(array, target, start, end):
    if start > end :
        return None
    
    mid = (start + end) // 2

    if (mid == (n - 1) or target < array[mid + 1]) and array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return last(array, target, start, mid -1)
    
    else:
        return last(array, target, mid + 1, end)

n, x = list(map(int, input().split()))
array = list(map(int, input().split()))

count = count_by_value(array, x)

if count == 0:
    print(-1)

else:
    print(count)
    '''


from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index =  bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = list(map(int, input().split()))
array = list(map(int, input().split()))

count =  count_by_range(array, x, x)

if count == 0:
    print(-1)

else:
    print(count)

