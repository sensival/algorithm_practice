# 레스토랑의 구조는 완전히 동그란 모양이고 외벽의 총 둘레는 n미터이며, 외벽의 몇몇 지점은 추위가 심할 경우 손상될 수도 있는 취약한 지점들이 있습니다. 
# 따라서 내부 공사 도중에도 외벽의 취약 지점들이 손상되지 않았는 지, 주기적으로 친구들을 보내서 점검을 하기로 했습니다. 다만, 빠른 공사 진행을 위해 점검 시간을 1시간으로 제한했습니다. 
# 친구들이 1시간 동안 이동할 수 있는 거리는 제각각이기 때문에, 최소한의 친구들을 투입해 취약 지점을 점검하고 나머지 친구들은 내부 공사를 돕도록 하려고 합니다. 
# 편의 상 레스토랑의 정북 방향 지점을 0으로 나타내며, 취약 지점의 위치는 정북 방향 지점으로부터 시계 방향으로 떨어진 거리로 나타냅니다. 또, 친구들은 출발 지점부터 시계, 혹은 반시계 방향으로 외벽을 따라서만 이동합니다.
# 외벽의 길이 n, 취약 지점의 위치가 담긴 배열 weak, 각 친구가 1시간 동안 이동할 수 있는 거리가 담긴 배열 dist가 매개변수로 주어질 때, 취약 지점을 점검하기 위해 보내야 하는 친구 수의 최소값을 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# n은 1 이상 200 이하인 자연수입니다.
# weak의 길이는 1 이상 15 이하입니다.
# 서로 다른 두 취약점의 위치가 같은 경우는 주어지지 않습니다.
# 취약 지점의 위치는 오름차순으로 정렬되어 주어집니다.
# weak의 원소는 0 이상 n - 1 이하인 정수입니다.
# dist의 길이는 1 이상 8 이하입니다.
# dist의 원소는 1 이상 100 이하인 자연수입니다.
# 친구들을 모두 투입해도 취약 지점을 전부 점검할 수 없는 경우에는 -1을 return 해주세요.

# 입출력 예
# n	    weak	        dist	     result
# 12	[1, 5, 6, 10]	[1, 2, 3, 4]	2
# 12	[1, 3, 4, 9, 10]	[3, 5, 7]	1

'''
def solution(n, weak, dist):
    answer = 0
    return answer
'''
from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)

    # 길이를 두배로 늘려서 원형으로 일자로 변경
    for i in range(length):
        weak.append(weak[i] + n) 

    # 투입할 친구수 초기화
    answer = len(dist) + 1

    # 0부터 length-1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 생성
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구 수
            position = weak[start] + friends[count - 1] # 친구가 점검하는 마지막 위치
            for index in range(start, start + length):
                if position < weak[index]: #친구가 점검할 수 있는 범위 밖에 weak이 있을때
                    count += 1 # 한명더 투입 
                    if count > len(dist): # 투입할 친구 없으면 break하고 다른 조합
                        break
                    position = weak[index] + friends[count - 1]
            answer =  min(answer, count) # 경우의 수가 외벽을 점검가능한 경우 for문 빠져나옴. 친구수 update

    if answer > len(dist):
        return -1
        
    return answer

def get_integer_list_from_input_with_brackets():
    while True:
        try:
            input_str = input("정수 리스트를 입력하세요 (대괄호 포함): ")
            
            # 입력 문자열에서 대괄호 제거 후 공백 제거, 쉼표로 분리하여 정수로 변환
            integer_list = [int(x) for x in input_str.replace("[", "").replace("]", "").replace(" ", "").split(",")]
            
            return integer_list
        except ValueError:
            print("올바른 형식으로 입력하세요. 예: [1, 2, 3]")
    
n = int(input())
weak = get_integer_list_from_input_with_brackets()
dist = get_integer_list_from_input_with_brackets()
print(solution(n, weak, dist))
