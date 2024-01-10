# 어피치는 문자열 압축에 대해 공부하고 있다. 문자열에서 같은 값이 연속해서 나타나면 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 나타내는것이다
# 예를들어 aabbaccc -> 2a2ba3c 인데 이러한 방식은 연속되는 문자가 없는경우 압축률이 낮다는 단점이 있다.
# 만약 문자열을 1개 이상단위로 잘라보면 ababcdcdababcdcd 는 1개 단위로 자르면 압축이 되지 않지만 2개단위로 자르면 2ab2cd2ab2cd로 압축될 수 있다.
# 문자열 s 가 주어질때 1개이상의 문자열을 잘라 압축한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution을 완성하시오
# 입력예시 1) aabbaccc  출력 7
# 입력예시 2) ababcdcdababcdcd  출력 9
# 입력예시 3) abcabcdede 출력 8 
# 입력예시 4) abcabcabcabcdededededede 출력 14
# 입력예시 5) xababcdcdababcdcd  출력 17
'''
def solution(s):
    answer = 0
    return answer
'''

# 나의 풀이
from collections import deque

def solution(s):
    answer =  len(s)
    string_list = []
    length = len(s)

    def push_str(q, s, start, end):
        for index in range(start, end): 
            q.append(s[index])
        return q

    def pop_str(q,count):
        str_q = ''
        str_q += (str(count) if count > 1 else '')
        while q:
            str_q += q.popleft()
        return str_q
    
    def slice_str(s, start, end):
        current = s[start:end]
        return current
        
    for step in range(1, (length//2)+1): # 간격 1 ~ 문자열 길이 절반 이하까지만
        string_now = ''
        queue = deque()
        count = 1
        queue = push_str(queue, s, 0, step)
        for i in range(step, length, step): # 큐에 하나씩 넣어서 비교
            compare = slice_str(s, i, min(i + step, length))
            # print("step",step, "i:",i,"--->", compare)

            if i + step < length and "".join(queue) == compare:
                count += 1

            elif i + step < length and "".join(queue) != compare:
                string_now += pop_str(queue, count)
                queue = push_str(queue, s, i, i + step)
                count = 1
                # print("strnow_step",step, "i:",i,"--->", string_now)

            else:
                # print("마지막")
                string_now += (pop_str(queue, count+1) if "".join(queue) == compare else pop_str(queue, count) + compare)

        # print(string_now)
        string_list.append(len(string_now))
        answer = min(string_list)

    return answer

s = input()
print(solution(s))



'''
# 내 코드 GPT가 수정한거??? 다른사람거 뱉은듯?

from collections import deque

def solution(s):
    answer = float('inf')  # 최솟값을 찾기 위해 초기값을 무한대로 설정
    for step in range(1, (len(s)//2)+1):
        compressed = ""
        prev = s[0:step]
        count = 1

        for i in range(step, len(s), step):
            current = s[i:i+step]

            if prev == current:
                count += 1
            else:
                compressed += str(count) + prev if count > 1 else prev
                prev = current
                count = 1

        compressed += str(count) + prev if count > 1 else prev
        answer = min(answer, len(compressed))

    return answer

s = input()
print(solution(s))
'''

'''
# 교재 풀이
def solution(s):
    answer = len(s)
    for step in range(1,len(s)//2+1):
        compressed = ""
        prev = s[0:step]
        count = 1

        for j in range(step, len(s), step):
            if prev ==s[j:j+step]:
                count +=1
            
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1

        compressed += str(count) + prev if count>= 2 else prev
        answer = min(answer, len(compressed))
    return answer

s = input()
print(solution(s))
'''