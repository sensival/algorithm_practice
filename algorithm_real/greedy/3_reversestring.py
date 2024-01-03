# 문자열 s는 모두 0과 1로 이루어져있다. 연속된 하나이상의 숫자 덩어리를 한번 뒤집어서 0은 1로, 1은 0으로 바꿀수 있다. 이때 문자열을 모두 같은 수로 만들려면 몇번의 뒤집기가 필요한지 구하시오
# 입력 예시 0001100 출력 1

# 나의 풀이
s = input()

result = 1

for i in range(1, len(s)):
    if s[i - 1] != s[i] :
        result += 1
        
    elif s[i - 1] == s[i] and i == len(s):
        continue

print(result//2)

# 교재 풀이
