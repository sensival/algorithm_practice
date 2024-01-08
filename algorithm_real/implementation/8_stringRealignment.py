# 알파벳 대문자와 숫자로만 주어진 문자열이 주어진다. 이때 모든 알파벳을 정렬하여 출력한 뒤에 모든 숫자를 더하여 이어 출력하는 프로그램을 작성하시오
# 입력 예시 K1KA5CB7 출력 ABCKK13
# 입력 예시 AJKDLSI412K4JSJ9D 출력 ADDIJJJKLSS20
 
# 나의 풀이
s = input()

string = []
number = []

for i in s:
    if ord(i) > 57:
        string.append(i)
    else:
        number.append(int(i))


string.sort()
a = sum(number)

for i in string:
    print(i, end='')
print(a)

# 교재 풀이

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

if value != 0: # 숫자가 아무것도 없는경우 출력하지 않도록 해야한다!!
    result.append(str(value))

print(''.join(result)) # char 형이 모인 list 출력 .join 사용