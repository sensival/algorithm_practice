
# n 이하의 모든수를 검사
def is_prime_number1(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

print(is_prime_number1(4))
print(is_prime_number1(7))

# n의 제곱근만 검사
import math
def is_prime_number2(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i  == 0:
            return False
    return True

print(is_prime_number2(4))
print(is_prime_number2(7))

# 에라토스테네스의 채

n = 1000
array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(2, n + 1):
    if array[i]:
        print(i, end=' ')

