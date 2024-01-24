# N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.
# 우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.
# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 
# 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.
# N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다.

# 출력
# 첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.

# 예제 입력 1 
# 2
# 5 6
# 0 0 1 0

# 예제 출력 1 
# 30
# 30

# 예제 입력 2 
# 3
# 3 4 5
# 1 0 1 0

# 예제 출력 2 
# 35
# 17

# 예제 입력 3 
# 6
# 1 2 3 4 5 6
# 2 1 1 1

# 예제 출력 3 
# 54
# -24

# 예제풀이 1 DFS
'''
n = int(input())

data = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div

    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)

    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i])) #나눌때는 나머지 제거 //으로 하면 -3//2가 -2로 나옴
            div += 1



dfs(1, data[0])

print(max_value)
print(min_value)
'''
# 예제 풀이 2 중복순열(product) 라이브러리

from itertools import product

n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

operators_list = list(product(['+', '-', '*', '/'], repeat=n - 1))


for operators in operators_list:
    now = data[0]
    i = 1
    op_count = [add, sub, mul, div]
 
    for i in range(1, n + 1):
        if i == n:
            min_value = min(min_value, now)
            max_value = max(max_value, now)

        else:
            if operators[i - 1] == '+' and op_count[0] > 0:
                now = now + data[i]
                i += 1
                op_count[0] -= 1

            elif operators[i - 1] == '-' and op_count[1] > 0:
                now = now - data[i]
                i += 1
                op_count[1] -= 1

            elif operators[i - 1] == '*' and op_count[2] > 0:
                now = now * data[i]
                i += 1
                op_count[2] -= 1

            elif operators[i - 1] == '/' and op_count[3] > 0:
                now = int(now / data[i])
                i += 1
                op_count[3] -= 1
            else:
                break

print(max_value)
print(min_value)
