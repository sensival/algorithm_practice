# 각 자리가 숫자로만 이루어진 문자열 s가 주어졌을때 왼쪽부터 오른쪽까지 문자 사이에 +나 x 를 넣어 만들 수 있는 가장 큰 수를 구하시오
# 입력예시 1) 02984 -> 576
# 입력예시 2) 567 -> 210

# 나의 풀이
s = input()
result = 0

for i in range(len(s)):
    print(int(s[i]))
    if s[i] == '0' or s[i] == '1' or result == 0 :
        result = result + int(s[i])
        print('if문: ', result)
    else:
        result = result * int(s[i])
        print('else문: ', result)

print(result)

