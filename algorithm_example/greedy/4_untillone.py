#어떠한 수 N을 1로 만들때까지 1 또는 2번의 연산을 몇번 수행해야하는가? 1)N에서 1을 뺀다. 2)N을 K로 나눈다(이것은 N/K가 나누어 떨어질 때 만 가능하다.) 
#입력예시 25 5 출력 2

n, k= map(int, input().split())
result=0

while True:
    target = (n//K)*k
    result += (n-target)
    n = target
    if n<k:
        break
    result += 1
    n//=k

result += (n-1)# 마지막 남은 수에 대하여 1씩 빼기
print(result)