# 게임의 캐릭터는 럭키스트레이트라는 기술이 있다. 이 기술은 점수 N을 반으로 나누었을때 오른쪽 자릿수의 합과 왼쪽 자릿수의 합이 동일한 경우 사용할 수 있습니다.(123402 -> 사용가능 )
# 현재 점수 N이 주어지면 럭키 스트레이트를 사용할 수 있는지 출력하는 프로그램을 작성하시오. 단 N은 짝수 자릿수인 수로 주어집니다
# 입력 예시 1) 123402 출력 LUCKY
# 입력 예시 2) 7755 출력 READY

# 나의 풀이
score = input()

mid = int(len(score)/2)
left = 0
right = 0
for i in range(mid):
    left += int(score[i])


for j in range(mid, len(score)):
    right += int(score[j])


if left == right:
    print("LUCKY")

else:
    print("READY")

# 교재 풀이
    
n = input()
length = len(n)
summary = 0

for i in range(length//2):
    summary +=(n[i])

for i in range(length//2, length):
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")

else:
    print("READY")
