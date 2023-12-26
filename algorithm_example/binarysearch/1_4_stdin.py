# 이진 탐색 문제는 데이터가 많고나 탐색 범워기 넓은 편이다. 예를 들어 데이터의 개수가 1000만개를 넘어가거나 담색범위의 크기가 1000억 이상이라면 이진탐색 알고리즘을 의심하자
# input() 함수는 동작속도가 느려서 이럴 경우엔 sys 라이브러리의 readline함수를 이용하면 시간 초과를 피할 수 있다.

import sys
input_data = sys.stdin.readline().rstrip() # 줄바꿈 기호가 입력되므로 rstrip()호출

print(input_data)