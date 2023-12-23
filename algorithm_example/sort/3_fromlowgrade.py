# 첫째 줄에 학생수가 입력된다. 둘째 줄부터 학생 이름과 성적이 입력되며 성적이 낮은 학생부터 순서대로 출력
# 입력 예시
# 2
# 홍길동 95
# 이순신 77 출력 이순신 홍길동


n = int(input())
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

array = sorted(array, key =lambda student: student[1])

for student in array:
    print(student[0], end = ' ')