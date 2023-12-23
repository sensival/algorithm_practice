# A와 B 배열이있다. n과 k가 첫 줄에 입력되고 다음줄부터 A와 B 배열이 순서대로 입력된다. 배열의 길이는 각각 n이며 두 배열은 K번 원소를 교환할 수 있다. 이때 A 배열이 최댓값이 되도록 원소를 교환하고 합을 출력
# 입력 예시
# 5 3 
# 1 2 5 4 3
# 5 5 6 6 5

# 나의 풀이
n,k= map(int, (input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
    A[i], B[i] = B[i], A[i]

sum = 0
for j in range(n):
    sum += A[j]

print(sum)

# 교재 풀이
n,k= map(int, (input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(k):
    if A[i] < B[i]: # 비교하고 바꿨어야 했다!
        A[i], B[i] = B[i], A[i]

    else:
        break


print(sum(A))


