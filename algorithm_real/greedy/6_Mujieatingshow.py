# 회전판에 먹어야 할 음식이 N개 있다. 각 음식에는 1부터 N까지의 번호가 있다. 
# 무지는 1번부터 음식을 먹기 시작하며 회전판은 번호가 증가하는 순서대로 무지앞에 음식을 갖다놓는다. 
# 마지막 번호의 음식을 먹은 후에는 다시 1번 음식이 무지 앞으로 온다.
# 무지는 음식 하나를 1초동안 섭취한 후 남은 음식은 두고 다음 음식을 먹는다. 다음 음식은 아직 남은 음식 중 가장 가까이있는 음식을 말한다.
# 무지가 먹방을 시작한지 K초 후에 방송이 잠시 중단되었다. 무지는 방송이 정상화 된 후 다시 방송을 이어갈 때 몇번 음식 부터 먹으면 되는지 알고자 한다.
# 음식을 모두 먹는데 필요한 시간이 담긴 배열 food_times, K가 매개변수로 주어질때 몇번 음식부터 다시 섭취하면 되는지 알려주는 solution함수를 완성하시오. 더 먹을 음식이 없다면 - 1
# 입력 예시 
# 3 1 2
# K 출력 1
'''
def solution(food_times, k):
    answer = 0
    return answer
'''
'''
# 나의 풀이
food_times = list(map(int, input().split()))
k = int(input())

def solution(food_times, k):
    answer = 0
    sec = 0 
    empty_plate = 0 

    while True:
        now = (sec + empty_plate) % len(food_times)
        if food_times[now] != 0:
            food_times[now] -= 1
            sec += 1
        
        else:
            if set(food_times) == {0}:
                answer = -1
                break
            else:
                empty_plate += 1

        if sec == k + 1:
            answer = now + 1
            break
    
    
    return answer

print(solution(food_times, k))
'''

# 교재 풀이

import heapq

food_times = list(map(int, input().split()))
k = int(input())

def solution(food_times, k):
    # 전체 음식의 시간이 K보다 작거나 같으면 -1
    if sum(food_times) <= k:
        return -1
    
    q =[]
    for i in range(len(food_times)):
        # 최소힙에 음식 시간과 번호 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0 # 먹기위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식
    length = len(food_times) # 남은 음식의 개수

    # sum_value +(현재 음식 시간 - 이전 음식 시간) * 현재 음식 갯수
    # 8 6 4 이고 15초면 가장 적은음식인 3번 음식은 다 먹되, 1, 2번 음식이 남으니 1, 2 번 중에 골라짐
    while sum_value + ((q[0][0] - previous) * length) <= k:
        # 최소 힙에서 pop
        now = heapq.heappop(q)[0]
        # 가장 작은 음식 시간 * 남은 음식 개수 
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q, key = lambda x:x[1]) # Key는 음식 번호
    return result[(k - sum_value) % length][1] # 다 비울 수 있는 음식은 다 먹고 난 뒤 남은 음식 중에 순서 정함. +1 안해도 됨

print(solution(food_times, k))