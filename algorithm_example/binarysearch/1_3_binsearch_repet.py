def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        
        elif array[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1

    return None # 찾으려는 원소가 없을때 마지막 루프에서 원소가 하나 남고 end= mid -1  or start = mid + 1 되면서 루프 탈출

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소가 존재하지 않습니다. ")

else:
    print(result+1)
    