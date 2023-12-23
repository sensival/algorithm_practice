# index[1]~index[n]을 순서대로 선택하여 앞의 인덱스 중 삽입될 자리 탐색

array=[7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i,0,-1):
        if array[j]<array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)