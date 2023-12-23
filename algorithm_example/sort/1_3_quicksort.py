#pivot 통해 partition을 만들고 pivot보다 큰 것과 작은 것을 양쪽 partition에서 교환

#1
array =[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and array[left] < array[pivot]: # 피봇보다 큰 데이터
            left += 1
        while right > start and array[right] >= array: # 피봇보다 작은 데이터
            right -= 1
        if left > right:
            array[right], array[pivot] =  array[pivot], array[right] # 엇갈렸다면 작은 데이터랑 피봇 교환
        else:
            array[right], array[left] =  array[left], array[right]

        quick_sort(array, start, right-1)
        quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)


#2
array =[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail= array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side =  [x for x in tail if x > pivot]

    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))
