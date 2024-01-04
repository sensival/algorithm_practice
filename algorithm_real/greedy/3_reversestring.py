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
# 전부 0으로 바꾸거나 전부 1로 바꾸는 것 중 더 적은 횟수를 가지는 경우를 계산

data = input()

count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data)-1):
    if data[i] != data[i + 1]:
        if data[i + 1] =='1':
            count0 += 1
        else:
            count1 += 1


print(min(count1,count0))


