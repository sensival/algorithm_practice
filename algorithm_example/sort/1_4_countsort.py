# min ~ max 크기의 리스트 생성, list[data]에 += 1 하면서 데이터가 몇번 등장했는지 count 최종적으로 순서대로 개수만큼 출력하며 정렬
# min과 max의 차이가 1000000 넘지 않는 경우에 효과적, 정수 dats 정렬에만 가능

array= [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count=[0]*(max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
