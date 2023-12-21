def recursion_function(i):
    if i==100:
        return
    print(i,'번 째 재귀함수에서',i+1,'번 째 재귀함수를 호출합니다.')
    recursion_function(i+1)
    print(i,'번 째 재귀함수를 종료합니다.')

recursion_function(1)
