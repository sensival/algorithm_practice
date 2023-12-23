# sorted
array= [7,5,9,0,3,1,6,2,9,1,4,8]

result= sorted(array)
print(result)



# sort
array= [7,5,9,0,3,1,6,2,9,1,4,8]

array.sort()
print(array)


# Key를 활용한 정렬
array =[ ('바나나', 2), ('사과', 5), ('당근',3)]

def setting(data):
    return data[1]

result = sorted(array, key = setting) # 
print(result)

'''
sorted() 함수에서 key 매개변수에 함수를 전달하면 해당 함수의 결과를 기준으로 정렬이 이루어집니다. 
여기서 setting 함수는 배열의 각 원소에 대해 두 번째 요소를 반환하도록 정의되어 있습니다. 이 함수는 key 매개변수로 사용되어 정렬 기준을 제공합니다.
'''
